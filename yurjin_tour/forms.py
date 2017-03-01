'''
Created on 2016-10-31
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''
#from __future__ import absolute_import, unicode_literals
#from django.utils.encoding import force_text

from django import forms
from django.utils import timezone
from django.forms.models import inlineformset_factory
from django.contrib.admin import widgets

from dal import autocomplete
from .models import Contract, Tourist

import dal

from django.conf import settings
from django.templatetags.i18n import language


class ContractForm(forms.ModelForm):
    class Meta:
        
        model = Contract
        #fields = ['contract_num', 'contract_date', 'tourist_list']
        #fields = ('__all__')
        fields = [
            #'manager',
            'contract_num', 'contract_date', 'client',
            'tour_begin_date', 'tour_finish_date',
            'contract_sum', 'prepayment_sum',
            'tourist_list', 'tour_operator', 'resort',
            'hotel_name','room_type','hotel_begin_date', 'hotel_finish_date',
            'board',
            'transfer','excursion','russian_guide','visa_support',
            'medical_insurance','non_departure_insurance']
        
        widgets = {
            #'contract_date': forms.SelectDateWidget(years=range(timezone.now().year-3,timezone.now().year+3)),
            #'contract_num': autocomplete,
            #'contract_date': forms.SelectDateWidget(),
            #'contract_date': widgets.AdminDateWidget(format='%d/%m/%Y'),
            
            'contract_date': widgets.AdminDateWidget(),
                        
            'manager': autocomplete.ModelSelect2(),
            'office': autocomplete.ModelSelect2(),
            'client': autocomplete.ModelSelect2(),
            'status': autocomplete.ModelSelect2(),
            
            'tour_begin_date': widgets.AdminDateWidget(),
            'tour_finish_date': widgets.AdminDateWidget(),
            
            
            'signatory': autocomplete.ModelSelect2(),
            'tourist_list': autocomplete.ModelSelect2Multiple(url='tourist_list'),
            #'tourist_list': TouristList(url='tourist_list'),
            'tour_operator': autocomplete.ModelSelect2(),
            'resort': autocomplete.ModelSelect2(),
            'hotel_begin_date': widgets.AdminDateWidget(),
            'hotel_finish_date': widgets.AdminDateWidget(),
            'room_type': autocomplete.ModelSelect2(),
            'board': autocomplete.ModelSelect2(),
            
            'doc_get_date': widgets.AdminDateWidget(),
                        
            
            
            
        }


