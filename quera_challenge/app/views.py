from django.db.models import Exists, OuterRef
from rest_framework import views
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jdatetime import datetime as jdatetime
from app.models import ChallengeItem, ChallengeTransaction, User
from app.serializers import ChallengeTransactionSerializer, ChallengeItemSerializer
from django.db import models, transaction


class ChallengeListAPIView(generics.ListAPIView):
    serializer_class = ChallengeItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        today = jdatetime.today().togregorian()
        user = self.request.user

        return ChallengeItem.objects.filter(date_to_display__date=today).annotate(
            user_is_done=Exists(
                ChallengeTransaction.objects.filter(user=user, challenge_item=OuterRef('pk'))
            )
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context



class CreateChallengeTransactionView(views.APIView):
    permission_classes = [IsAuthenticated]  
    
    def post(self, request):
        # user = request.user
        user = User.objects.first()
        
        challenge_item_ids = request.data.get('challenge_item_ids')

        if not challenge_item_ids:
            return Response(
                {'error': 'challenge_item_ids must be provided.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        challenge_items = ChallengeItem.objects.filter(id__in=challenge_item_ids)

        if challenge_items.count() != len(challenge_item_ids):
            return Response(
                {'error': 'One or more challenge_item_ids are invalid.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        existing_transactions = ChallengeTransaction.objects.filter(
            user=user,
            challenge_item__in=challenge_items
        )

        if existing_transactions.exists():
            return Response(
                {'error': 'You have already completed one or more of these challenge items.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # new_transactions = [
        #     ChallengeTransaction(user=user, challenge_item=challenge_item)
        #     for challenge_item in challenge_items
        # ]
        # transactions = ChallengeTransaction.objects.bulk_create(new_transactions)
        with transaction.atomic():
            transactions = []
            for challenge_item in challenge_items:
                transactions.append(ChallengeTransaction.objects.create(user=user, challenge_item=challenge_item))

        serializer = ChallengeTransactionSerializer(transactions, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
