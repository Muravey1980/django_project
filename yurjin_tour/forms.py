'''
Created on 2016-10-31
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''
#from __future__ import absolute_import, unicode_literals
#from django.utils.encoding import force_text
#from __future__ import __all__

#import dal
#from django.conf import settings
#from django.templatetags.i18n import language

#from django.utils import timezone
#from django.forms.models import inlineformset_factory
#from django.forms.models import modelformset_factory

from django.core.exceptions import ValidationError

from django import forms
from django.contrib.admin import widgets
from dal import autocomplete
from .models import Contract, Tourist, Manager, Payment #, PaymentMethod


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        #fields = ['contract_num', 'contract_date', 'tourist_list']
        #fields = ('__all__')
        fields = [
            #'manager',
            #'contract_num', 
            'contract_date', 'client',
            'tour_begin_date', 'tour_finish_date',
            'contract_sum', 
            #'prepayment_sum',
            'tourist_list', 'tour_operator', 'resort',
            'hotel_name','room_type','hotel_begin_date', 'hotel_finish_date',
            'board',
            'transfer','excursion','russian_guide','visa_support',
            'medical_insurance','non_departure_insurance',
            #'payments'
            ]
        
        widgets = {
            #'contract_date': forms.SelectDateWidget(years=range(timezone.now().year-3,timezone.now().year+3)),
            #'contract_num': autocomplete,
            #'contract_date': forms.SelectDateWidget(),
            #'contract_date': widgets.AdminDateWidget(format='%d/%m/%Y'),
            
            'contract_date': widgets.AdminDateWidget(),
                        
            #'manager': autocomplete.ModelSelect2(),
            #'office': autocomplete.ModelSelect2(),
            'client': autocomplete.ModelSelect2(),
            'status': autocomplete.ModelSelect2(),
            
            'tour_begin_date': widgets.AdminDateWidget(),
            'tour_finish_date': widgets.AdminDateWidget(),
            
            
            #'signatory': autocomplete.ModelSelect2(),
            'tourist_list': autocomplete.ModelSelect2Multiple(url='tourist_list'),
            #'tourist_list': TouristList(url='tourist_list'),
            'tour_operator': autocomplete.ModelSelect2(),
            'resort': autocomplete.ModelSelect2(),
            'hotel_begin_date': widgets.AdminDateWidget(),
            'hotel_finish_date': widgets.AdminDateWidget(),
            'room_type': autocomplete.ModelSelect2(),
            'board': autocomplete.ModelSelect2(),
            
            #'doc_get_date': widgets.AdminDateWidget(),
        }

    def clean(self):
        cleaned_data = super(ContractForm, self).clean()
        if cleaned_data["contract_sum"] < 0:
            raise ValidationError("Сумма контракта не может быть меньше нуля",code = "invalid")
        #if cleaned_data["prepayment_sum"] < 0:
        #    raise ValidationError("Сумма предоплаты не может быть меньше нуля",code = "invalid")    
        #if cleaned_data["contract_sum"] < cleaned_data["prepayment_sum"]:    
        #    raise ValidationError("Сумма предоплаты не может быть больше суммы контракта",code = "invalid")
        if cleaned_data["tour_finish_date"] and cleaned_data["tour_begin_date"]:
            if cleaned_data["tour_finish_date"] < cleaned_data["tour_begin_date"]:
                raise ValidationError("Дата окончания тура не может быть меньше даты начала тура",code = "invalid")
        if cleaned_data["hotel_finish_date"] and cleaned_data["hotel_begin_date"]:    
            if cleaned_data["hotel_finish_date"] < cleaned_data["hotel_begin_date"]:
                raise ValidationError("Дата выезда из отеля не может быть меньше даты въезда в отель",code = "invalid")
        if cleaned_data["hotel_begin_date"] and cleaned_data["tour_begin_date"]:    
            if cleaned_data["hotel_begin_date"] < cleaned_data["tour_begin_date"]:
                raise ValidationError("Дата въезда в отель не может быть меньше даты начала тура ",code = "invalid")
        if cleaned_data["tour_finish_date"] and cleaned_data["hotel_finish_date"]:    
            if cleaned_data["tour_finish_date"] < cleaned_data["hotel_finish_date"]:
                raise ValidationError("Дата окончания тура не может быть меньше даты выезда из отеля",code = "invalid")
            
        return cleaned_data


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        #fields = ('__all__')
        exclude = ['office',]
        
        widgets = {    
            'birthdate': widgets.AdminDateWidget(),
            'passport_date': widgets.AdminDateWidget(),
            'international_passport_date_of_expiry': widgets.AdminDateWidget(),
            }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
                'contract',
                'payment_method',
                'payment_sum'
                ]
        
        widgets = {
            #'payment_date': widgets.AdminDateWidget(),
            #'payment_method': autocomplete.ModelSelect2(),
            'contract': autocomplete.ModelSelect2(),
            }
    
    def clean(self):
        cleaned_data = super(PaymentForm, self).clean()
        if cleaned_data["payment_sum"] <= 0:
            raise ValidationError("Сумма платежа должна быть положительным числом",code = "invalid")        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['last_name', 'first_name', 'mid_name', 'full_name_r']


#PaymentFormset = modelformset_factory(Payment, form=PaymentForm,can_delete=True)