from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^signup/$', views.signup, name='signup')
]
