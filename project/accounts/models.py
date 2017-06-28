from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, unique=True)
    follow_set = models.ManyToManyField('self',
                                        blank=True,
                                        through='Relation',
                                        symmetrical=False,)

    def __str__(self):
        return self.nickname


class Relation(models.Model):
    from_user = models.ForeignKey(Profile, related_name='follower_user')
    to_user = models.ForeignKey(Profile, related_name='follow_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {}".format(self.from_user, self.to_user)
