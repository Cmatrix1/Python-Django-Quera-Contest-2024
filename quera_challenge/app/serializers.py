from jdatetime import datetime as jdatetime
from rest_framework import serializers
from .models import Challenge, ChallengeItem, ChallengeTransaction


class ChallengeItemSerializer(serializers.ModelSerializer):
    is_done = serializers.BooleanField(source='user_is_done')  # Use the annotated field
    jalali_date_to_display = serializers.SerializerMethodField()

    class Meta:
        model = ChallengeItem
        fields = ('id', 'title', 'description', 'jalali_date_to_display', 'is_done')

    def get_jalali_date_to_display(self, obj: ChallengeItem):
        return jdatetime.fromgregorian(datetime=obj.date_to_display).strftime('%Y/%m/%d')


class ChallengeTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeTransaction
        fields = ('id', 'user', 'challenge_item', 'created_at', 'updated_at')
