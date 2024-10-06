from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    point_earned = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.username

