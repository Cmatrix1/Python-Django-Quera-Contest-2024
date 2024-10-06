from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    point = models.IntegerField()
    award = models.ForeignKey('app.Award', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class ChallengeItem(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_to_display = models.DateTimeField()

    def __str__(self):
        return self.title


class ChallengeTransaction(models.Model):
    challenge_item = models.ForeignKey(ChallengeItem, on_delete=models.CASCADE)
    user = models.ForeignKey('app.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} completed {self.challenge_item.title}'
    

