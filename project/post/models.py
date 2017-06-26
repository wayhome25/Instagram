from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import re


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = ProcessedImageField(upload_to='post/post/%Y/%m/%d',
                                processors=[ResizeToFill(600, 600)],
                                format='JPEG',
                                options={'quality': 90})
    content = models.CharField(max_length=140, help_text="최대 140자 입력 가능")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like') # post.like_set 으로 접근 가능

    class Meta:
        ordering = ['-created_at']

    # NOTE: content에서 tags를 추출하여, Tag 객체 가져오기, 신규 태그는 Tag instance 생성, 본인의 tag_set에 등록,
    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return
        for t in tags:
            self.save()
            tag, tag_created = Tag.objects.get_or_create(name=t)
            if not self.tag_set.filter(id=tag.id).exists():
                self.tag_set.add(tag) #NOTE: ManyToManyField 에 인스턴스 추가

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
