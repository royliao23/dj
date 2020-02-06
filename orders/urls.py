
from . import views
from django.urls import path
from django.conf.urls import include, url


app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('create/<str:cart>', views.order_create2, name='order_create2'),
    url(r'^likePost/(?P<pk>[0-9]+)/$', views.likePost, name='likepost'),   # likepost view at /likepost
    url(r'^postlist/$', views.postlist, name='postlist'),
    url(r'^postlist/ajax2/', views.ajax2,name='aj2'),
    url(r'^commentpost/(?P<pk>[0-9]+)/$', views.commentpost, name='commentpost'),
    
]