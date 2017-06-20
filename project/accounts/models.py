from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    nickname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nickname
