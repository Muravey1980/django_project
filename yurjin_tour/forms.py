'''
Created on 2016-10-31
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''
from .models import Contract, Tourist
from django import forms
from django.utils import timezone

from django.forms.models import inlineformset_factory

#from django_select2.forms import Select2Widget, Select2MultipleWidget, ModelSelect2MultipleWidget
#from django.contrib.admin import widgets
#import 

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['contract_num', 'contract_date', 'tourist_list']
        #widgets = {
        #    'contract_date': forms.SelectDateWidget(years=range(timezone.now().year,timezone.now().year+3)),
        #    #'tourist_list': forms.CheckboxSelectMultiple()
        #    #'tourist_list': widgets.FilteredSelectMultiple('tourist_list',True)
        #    #'tourist_list': ModelSelect2MultipleWidget,
        #}

ContractTouristFormSet = inlineformset_factory(Tourist,Contract,fields = ['tourist_list'],extra=0, can_delete=True)
