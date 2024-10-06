from django.db import models


class Award(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class AwardTransaction(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    user = models.ForeignKey('app.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} received {self.award.name}'

