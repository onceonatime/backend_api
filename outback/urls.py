"""outback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from relics.views import DatasList, SiteList, TimesList, CityList, CoordinateList, ProxyImage, ProxyDetail
# from outback.relics.views import DatasList

urlpatterns = [
    path('', DatasList.as_view(), name='datas'),
    path('images/', ProxyImage.as_view(), name="images"),
    path('detail/', ProxyDetail.as_view(), name="detail"),
    path('coordinate/', CoordinateList.as_view(), name="coord"),
    path('sites/<city>/', CityList.as_view(), name="citys"),
    path('sites/<city>/<town>/', SiteList.as_view(), name="sites"),
    path('times/<times>/', TimesList.as_view(), name="times"),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls'))
]
