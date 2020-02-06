from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views
app_name = 'payments'
urlpatterns = [
	#path('/homep', views.callback, name='homep'),
    path('/homep', views.HomePageView.as_view(), name='homep'),
    path('charge/', views.charge, name='charge'), # new
    url(r'^create/$', views.order_create, name='order_create'),

   # url(r'^paypal/', include('paypal.standard.ipn.urls')),
	path('/payment_process', views.payment_process, name='payment_process' ),
	url(r'^payment_done/$', TemplateView.as_view(template_name= "payments/payment_done.html"), name='payment_done'),
	url(r'^payment_canceled/$', TemplateView.as_view(template_name= "paymments/payment_cancelled.html"), name='payment_canceled'),

]