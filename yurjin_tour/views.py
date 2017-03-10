from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from django.core.urlresolvers import reverse_lazy

from .models import Contract, Tourist, Manager
from . import forms


from django.template.context_processors import request


from dal import autocomplete
from config import auth_user


class ContractPdfPrint(generic.TemplateView): 
    template_name = "yurjin_tour/contract_print.html"


class TouristList(autocomplete.Select2QuerySetView):
    
    def get_queryset(self):
        qs = Tourist.objects.all()

        if self.q:
            qs = qs.filter(last_name__istartswith=self.q)
            
        return qs


class ContractEditView(generic.UpdateView):
    template_name = 'yurjin_tour/contract_edit.html'
    model = Contract
    form_class=forms.ContractForm
    success_url = reverse_lazy('yurjin_tour:index')
    success_message = "Договор успешно изменен"        


class ContractCreateView(generic.CreateView):
    def get_num(self):
        #last_contract = Contract.objects.latest(field_name='contract_date')
        last_contract = Contract.objects.order_by('-contract_date','-contract_num')[0:1].get()
        if (last_contract.contract_date.year==timezone.datetime.today().year and last_contract.contract_date.month==timezone.datetime.today().month):
            #new_num=last_contract.contract_date.month
            new_num=last_contract.contract_num+1
        else:
            new_num=1
            #new_num='false'
        return new_num #last_contract.contract_date
    #last_contract.contract_num+1 if last_contract.contract_date.year==timezone.datetime.today().year else 1
        #return last_contract.contract_date.year 
        #return timezone.datetime.today().year==last_contract.contract_date.year

    def form_valid(self, form):
        form.instance.manager = self.request.user.manager
        form.instance.office = self.request.user.manager.manager_office
        form.instance.signatory = self.request.user.manager.manager_office.tour_agency.director
        form.instance.contract_num = self.get_num()
        
        #form.instance.
        return super(ContractCreateView, self).form_valid(form)    
  
    template_name = 'yurjin_tour/contract_edit.html'
    model = Contract    
    initial = {
                'contract_date': timezone.datetime.today(),
                #'contract_num': get_num()
                }
    

    
    
    #def get_num():
    #    last_contract = Contract.objects.latest(field_name='contract_date')
    #    return last_contract.contract_num+1 if last_contract.contract_date.year==timezone.datetime.today().year else 1 
    
    
               #'contract_date':timezone.datetime.today()}
               #Contract.objects.latest(field_name='contract_date').contract_num+1, 'contract_date':timezone.datetime.now()}
    #from django.db.models import Max
    #Contract.objects.filter(contract_num__year=timezone.datetime.year(timezone.datetime.now())).order_by('-number')[0]+1
    #initial = {'contract_num':Contract.objects.filter().max() (field_name='contract_date').contract_num+1}
    form_class=forms.ContractForm
    success_url = reverse_lazy('yurjin_tour:index')
    success_message = "Договор успешно создан"        


class ContractDeleteView(generic.DeleteView):
    model = Contract
    template_name = "yurjin_tour/contract_delete.html"
    #pk_url_kwarg = "contract_id"

    #template_name = 'yurjin_tour/contract_edit.html'
    
    #form_class=forms.ContractForm
    success_url = reverse_lazy('yurjin_tour:index')
    #success_message = "Договор успешно удален"    
    

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
    #template_name = 'yurjin_tour/contract_list.html'


class ContractListView(generic.ListView):
    #template_name = 'yurjin_tour/contract_list.html'
    #context_object_name = 'latest_contract_list'
    
    #model = Contract
    queryset = Contract.objects.order_by('-contract_date')

    #def get_queryset(self):
    #    Для фильтрации по пользователю - self.request.user
    #    self.manager = get_object_or_404(Manager, id=1)
    #    return Contract.objects.filter(manager = self.manager).order_by('-input_date')[:5]


class TouristListView(generic.ListView):
    #template_name = 'yurjin_tour/tourist_list.html'
    model = Tourist
    paginate_by = 20
    queryset = Tourist.objects.order_by('last_name', 'first_name', 'mid_name')


class TouristEditView(generic.UpdateView):
    template_name = 'yurjin_tour/tourist_edit.html'
    model = Tourist
    form_class=forms.TouristForm
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Данные туриста успешно изменен"        


class TouristCreateView(generic.CreateView):    
    template_name = 'yurjin_tour/tourist_edit.html'
    model = Tourist
    form_class=forms.TouristForm
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Даннные туриста успешно создан"        


class TouristDeleteView(generic.DeleteView):
    model = Tourist
    template_name = "yurjin_tour/tourist_delete.html"
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Турист успешно удален"    
    
    





    

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


