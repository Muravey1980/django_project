'''
Created on 2016-10-26
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''

from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'yurjin_tour'
urlpatterns = [
    url(r'^login/', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {"next_page": 'yurjin_tour:login'}, name = 'logout'),
    
    
    
    url(r'^(?P<page>[0-9])*$', login_required(views.IndexView.as_view()), name='index'),
    #url(r'^contracts$', views.ContractListView.as_view(), name='contract_list'),
    url(r'^tourists/$', login_required(views.TouristListView.as_view()), name='tourist_list'),
    url(r'^contracts/$', login_required(views.ContractArchiveIndexView.as_view()), name='contract_archive'),
    url(r'^contracts/(?P<year>[0-9]{4})/$', login_required(views.ContractYearArchiveView.as_view()), name='contract_archive_year'),
    url(r'^contracts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', login_required(views.ContractMonthArchiveView.as_view()), name='contract_archive_month'),
    
    url(r'^contract/(?P<pk>[0-9]+)/print/$', login_required(views.ContractDetailView.as_view()), name='contract_print'),
    
    
    #url(r'^contract/(?P<pk>[0-9]+)/edit_test/$', views.ContractEditTest.as_view(), name='edit_test'),
    
    #url(r'^contract/(?P<contract_id>[0-9]+)/save$', views.contract_save, name='contract_save'),
    
    url(r'^contract/(?P<pk>[0-9]+)/print/$', login_required(views.ContractPdfPrint.as_view()), name='contract_pdf_print'),


    url(r'^contract/(?P<pk>[0-9]+)/edit/$', permission_required('yurjin_tour.edit_contract')(views.ContractEditView.as_view()), name='contract_edit'),
    url(r'^contract/add/$', permission_required('yurjin_tour.add_contract')(views.ContractCreateView.as_view()),name = 'contract_add'),
    url(r'^contract/(?P<pk>[0-9]+)/delete/$', permission_required('yurjin_tour.delete_contract')(views.ContractDeleteView.as_view()),name = 'contract_delete'),
    
    
    url(r'^tourist/(?P<pk>[0-9]+)/edit/$', permission_required('yurjin_tour.edit_contract')(views.TouristEditView.as_view()), name='tourist_edit'),
    url(r'^tourist/add/$', permission_required('yurjin_tour.add_contract')(views.TouristCreateView.as_view()),name = 'tourist_add'),
    url(r'^tourist/(?P<pk>[0-9]+)/delete/$', permission_required('yurjin_tour.delete_contract')(views.TouristDeleteView.as_view()),name = 'tourist_delete'),
    

    #url(r'^heavy_select2_multiple_widget/$',views.TemplateFormView.as_view(form_class=HeavySelect2MultipleWidgetForm, success_url='/'),name='heavy_select2_multiple_widget'),
       
]
