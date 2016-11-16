'''
Created on 2016-10-26
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''

from django.conf.urls import url

from . import views

app_name = 'yurjin_tour'
urlpatterns = [
    # ex: /yurjin_tour/
    url(r'^(?P<page>[0-9])*$', views.IndexView.as_view(), name='index'),
    # ex: /contract/1/

    #url(r'^contracts$', views.ContractListView.as_view(), name='contract_list'),
    url(r'^contracts/$', views.ContractArchiveIndexView.as_view(), name='contract_archive'),
    url(r'^contracts/(?P<year>[0-9]{4})/$', views.ContractYearArchiveView.as_view(), name='contract_archive_year'),
    url(r'^contracts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.ContractMonthArchiveView.as_view(), name='contract_archive_month'),
    
    url(r'^contract/(?P<pk>[0-9]+)/print/$', views.ContractDetailView.as_view(), name='contract_print'),
    url(r'^contract/(?P<pk>[0-9]+)/edit/$', views.ContractEditView.as_view(), name='contract_edit'),
    
    url(r'^contract/(?P<contract_id>[0-9]+)/save$', views.contract_save, name='contract_save'),
]
