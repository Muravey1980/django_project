'''
Created on 2016-10-31
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''
from .models import Contract
from django import forms

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['input_date', 'client']
        
