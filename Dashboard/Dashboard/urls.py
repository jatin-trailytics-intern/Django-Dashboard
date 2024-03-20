"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Dash.views import *

urlpatterns = [
    path("", enter, name='start'),
    path('admin/', admin.site.urls),
    path('amzon/', amazon_Home, name='amzhome'),
    path('flipkart/', flipk_Home, name='flipkhome'), 
    path('con1/', content1, name='con'),
    path('adgroup/', Adsgroup, name='adgroup'),
    path('con2/', content3, name='con2'),
    path('product/', amazon_Product, name='product'), 
    path('failed/', page_404, name='404')

]
