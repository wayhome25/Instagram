from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    # url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'login'}),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^account_change/$', views.account_change, name='account_change'),
    url(r'^follow/$', views.follow, name='follow'),
]
