"""FirstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
# this canalso be imported as from .views import home 
# then     path('', views.home) will be     path('', home),


# in FirstApp/urls.py it is of type Function Views
#     path('firstapp/',include('FirstApp.urls')), is of type  URLconf 
#     path('firstapp/',include('FirstApp.urls')) neeeds to be added only once 
# once added it links firstapp/ to urls in firstapp.urls 
# next for example if u have  path('abc ',views.index) in FirstApp/urls then that can be acceses as
# /firstapp/abc
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/',include('FirstApp.urls')),
    path('', views.home),
    path('secondapp/',include('SecondApp.urls')),



]


