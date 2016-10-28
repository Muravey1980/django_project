'''
Created on 2016-10-26
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''

from django.conf.urls import url

from . import views

app_name = 'yurjin_tour'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /contract/1/
    url(r'^contract/(?P<contract_id>[0-9]+)/$', views.contract_detail, name='detail'),
]
