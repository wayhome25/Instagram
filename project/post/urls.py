from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^explore/tags/(?P<tag>\w+)/$', views.post_search, name='post_search'),
    url(r'^(?P<pk>\d+)/like/$', views.post_like, name='post_like'), 
]
