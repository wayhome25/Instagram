from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from accounts.models import Profile


# social 회원가입시 Profile 인스턴스를 함께 생성하도록 오버라이딩
class MyAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super(MyAdapter, self).save_user(request, sociallogin)
        Profile.objects.create(
            user = user,
            nickname = user.username)
        user.save()
