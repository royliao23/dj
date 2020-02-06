from django.urls import path
from. import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'

urlpatterns = [
	path('',views.home, name='home'),
	path('createpost/',views.createpost, name='createpost') ,
	path('confirm',views.customerorder, name='co') ,
	url(r'^list/$',views.product_list, name='product_list') ,
	url(r'^list/(?P<pk>[0-9]+)/$',views.category_select, name='category_select'),
	url(r'^contact/$', views.contactview, name='contact'),
	path('about/',views.about, name='about') ,
	#path('contact/',views.contact, name='contact') ,
	#path('contact/r^(?P<mid>[1-9]+)/$',views.mid, name='mid') ,
	#path('contact/page<int:num>/', views.mid),
	#url(r'^contact/(?P<mid>\d+)/$', views.mid, name='mid'),
	#url(r'^details/(?P<key>[0-9]+)/$', views.mid, name='mid'),
	url(r'^index/$',views.IndexView.as_view(), name='index') ,
	#url(r'^list$',views.product_list, name='list') ,
	url(r'^indexproducts/$',views.pindex, name='indexp') ,
	#url(r'^indexproducts/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='productdetail') ,
	url(r'^indexproducts/(?P<pk>[0-9]+)/$',views.product_detail, name='productdetail') ,
	#url(r'^indexproducts/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='pdetail') ,
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='mid'),
	url(r'^index/add/$', views.MusicianCreate.as_view(), name='addm'),
	#path('index/',views.index, name='index') ,
	#url(r'^indexstar/',views.indexs, name='indexs'),
	path('indexstar/',views.indexs, name='indexs'),
	url(r'^indexstar/f/$', views.indexstar, name='indexf'),
	url(r'^blogadd/$', views.showform, name='blogadd'),
	url(r'^(?P<id>\d+)/edit/$', views.editpost, name='editpost'),
	url(r'^(?P<id>\d+)/delete/$', views.musician_delete_view, name='deletepost'),
	url(r'^test1/$',views.test1, name='test1') ,
	url(r'^indexproducts/(?P<pk>[0-9]+)/confirm.html',views.confirm, name='confirm') ,
	url(r'^try/$', views.aindex, name='try'),
    url(r'^ajax/', views.ajax,name='aj'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#from django.conf.urls import url
#from django.contrib import admin

#from mysite.views import hello

#urlpatterns = [
#   url(r'^admin/', admin.site.urls),
#   url(r'^hello/$', hello),
#