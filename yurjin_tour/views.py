#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from yurjin_tour import forms

from django.core.urlresolvers import reverse_lazy

from .models import Contract, Tourist, Manager

#from .forms import ContractForm

from django.template.context_processors import request
from django.http import HttpResponse


class ContractPdfPrint(generic.TemplateView): 
    template_name = "yurjin_tour/contract_print.html"
    pass    


class ContractEditView(generic.UpdateView):
    template_name = 'yurjin_tour/contract_edit.html'
    model = Contract
    form_class=forms.ContractForm
    tourist_formset = forms.ContractTouristFormSet()
    #form_class=forms.ContractTouristFormSet()
    
    #fields =
    #fields = Contract._meta.get_all_field_names()
    #fields = list(Contract._meta.get_fields())
    #fields = [field.name for field in Contract._meta.local_fields]
    #get_all_field_names(Contract)
    #exclude = ('contract_id',)
    #widgets = {'contract_date': SelectDateWidget(years=range(1940, 2014))}


    success_url = reverse_lazy('yurjin_tour:index')
    success_message = "Новость успешно изменена"
    
    #def get_form(self, form_class):
    #    from django import forms
    #    form = super(ContractEditView, self).get_form(form_class)
    #    form.fields['contract_date'].widget = forms.SelectDateWidget()
    #    return form

    #def get(self, request, *args, **kwargs):
    #    self.object = self.get_object()
    #    tourist_formset = self.get_form(ContractTouristFormSet)
        



class ContractArchiveIndexView(generic.ArchiveIndexView):
    model = Contract
    date_field = 'contract_date'


class ContractYearArchiveView(generic.YearArchiveView):
    model = Contract
    date_field = 'contract_date'
    

class ContractMonthArchiveView(generic.MonthArchiveView):
    model = Contract
    date_field = 'contract_date'
    month_format = '%m' 
    context_object_name = 'contract_list'
    template_name = 'yurjin_tour/contract_list.html'


class ContractListView(generic.ListView):
    #template_name = 'yurjin_tour/contract_list.html'
    #context_object_name = 'latest_contract_list'
    
    #model = Contract
    queryset = Contract.objects.order_by('-contract_date')

    #def get_queryset(self):
    #    Для фильтрации по пользователю - self.request.user
    #    self.manager = get_object_or_404(Manager, id=1)
    #    return Contract.objects.filter(manager = self.manager).order_by('-input_date')[:5]


class IndexView(generic.ListView):
    template_name = 'yurjin_tour/index.html'
    model = Contract
    #context_object_name = 'latest_contract_list'
    
    
    paginate_by = 10
    
    #if (get(page)==None): page=1
    
    def get_queryset(self):
        return Contract.objects.filter(
            contract_date__lte=timezone.now()
        ).order_by('-contract_date','-contract_num')
        

class ContractDetailView(generic.DetailView):
    model = Contract
    template_name = 'yurjin_tour/contract_detail.html'
    
    def get_queryset(self):
        return Contract.objects.filter(contract_date__lte=timezone.now())
    

def contract_save(request, contract_id):
    pass


