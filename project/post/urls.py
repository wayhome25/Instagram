from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<username>\w+)/list/$', views.my_post_list, name='my_post_list'),
    url(r'^(?P<username>\w+)/list/detail/$', views.my_post_list_detail, name='my_post_list_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^comment/new/$', views.comment_new, name='comment_new'),
    url(r'^comment/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^comment/more/$', views.comment_more, name='comment_more'),
    url(r'^explore/tags/(?P<tag>\w+)/$', views.post_list, name='post_search'),
    url(r'^like/$', views.post_like, name='post_like'),
    url(r'^follow/$', views.follow_post_list, name='follow_post_list'),
    url(r'^(?P<username>\w+)/list/follow/$', views.follow_list, name='follow__list'),
]
