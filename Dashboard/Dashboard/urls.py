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
    path('portf/', Portfolio, name='portfolio'),
    path('Campagins/', Campagins, name='camp'),
    path('product/', Product, name='product'),
    path('adgroup/', Adsgroup, name='adgroup'),
    path('Rules/', Rule, name='rule'), 
    path('keywrd/', keywords, name='key'),  

    path('keywrd_analytics/', keywordAnalytics, name='keywrd_analytics'),  
    path('failed/', page_404, name='404')

]
