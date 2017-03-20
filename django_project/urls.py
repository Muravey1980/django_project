"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import javascript_catalog
from yurjin_tour.views import TouristList

urlpatterns = [
    url(r'^jsi18n', javascript_catalog, {'packages':('yurjin_tour.apps.YurjinTourConfig',) }),
    
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^yurjin_tour/', include('yurjin_tour.urls')),    
    
    url(r'^tourist_list/$',TouristList.as_view(),name='tourist_list'),
    
    
]
