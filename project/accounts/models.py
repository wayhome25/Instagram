from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('닉네임', max_length=30, unique=True)
    follow_set = models.ManyToManyField('self',
                                        blank=True,
                                        through='Relation',
                                        symmetrical=False, )
    picture = ProcessedImageField(upload_to=user_path,
                                  processors=[ResizeToFill(150, 150)],
                                  format='JPEG',
                                  options={'quality': 90},
                                  blank=True,
                                  )
    about = models.CharField(max_length=150, blank=True)
    GENDER_CHOICES = (
        ('선택 안 함', '선택 안 함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField('성별(선택사항)', max_length=10, choices=GENDER_CHOICES, default='N')

    def __str__(self):
        return self.nickname

    @property
    def get_follower(self):
        return [i.from_user for i in self.follower_user.all()]

    @property
    def get_following(self):
        return [i.to_user for i in self.follow_user.all()]

    @property
    def follower_count(self):
        return len(self.get_follower)

    @property
    def following_count(self):
        return len(self.get_following)

    def is_follower(self, user):
        return user in self.get_follower

    def is_following(self, user):
        return user in self.get_following


class Relation(models.Model):
    from_user = models.ForeignKey(Profile, related_name='follow_user')
    to_user = models.ForeignKey(Profile, related_name='follower_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {}".format(self.from_user, self.to_user)

    class Meta:
        unique_together = (
            ('from_user', 'to_user')
        )
