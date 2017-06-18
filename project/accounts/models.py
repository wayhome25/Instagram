from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # NOTE: User에서 접근시 활용 (user.profile.nickname)
    nickname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nickname
