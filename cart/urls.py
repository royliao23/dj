from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    #url(r'^remove/(?P<cartno>\d+'*'+)/$', views.cart_remove, name='cart_remove2'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path('remove/<str:cartno>', views.cart_remove, name='cart_remove2'),
    path('add/<str:cartno>', views.cart_add2, name='cart_add2'),
]
