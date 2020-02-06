"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from newapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('', include('pages.urls')),
    path('payments', include('payments.urls')), 
    url(r'^employees/', views.employeeList.as_view(),name='emplist'),
    #url(r'^g/$', views.gv(), name='g'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
#   url(r'^admin/', admin.site.urls),
#]