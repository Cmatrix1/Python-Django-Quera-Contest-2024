from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import ChallengeTransaction, ChallengeItem, AwardTransaction, User

@transaction.atomic
@receiver(post_save, sender=ChallengeTransaction)
def create_award_transaction(sender, instance: ChallengeTransaction, created, **kwargs):
    if created:
        user: User = instance.user
        challenge_item = instance.challenge_item
        challenge = challenge_item.challenge

        total_items = ChallengeItem.objects.filter(challenge=challenge).count()
        completed_items = ChallengeTransaction.objects.filter(
            user=user,
            challenge_item__challenge=challenge
        ).count()
        

        if total_items == completed_items:
            award = challenge.award

            AwardTransaction.objects.create(
                award=award,
                user=user
            )
            user.point_earned += challenge.point
            user.save()
                


