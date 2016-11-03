#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Contract, Tourist, Manager

#from .forms import ContractForm

from django.template.context_processors import request


class ContractArchiveIndexView(generic.ArchiveIndexView):
    model = Contract
    date_field = 'input_date'


class ContractYearArchiveView(generic.YearArchiveView):
    model = Contract
    date_field = 'input_date'
    

class ContractMonthArchiveView(generic.MonthArchiveView):
    model = Contract
    date_field = 'input_date'
    month_format = '%m' 
    context_object_name = 'contract_list'
    template_name = 'yurjin_tour/contract_list.html'


class ContractListView(generic.ListView):
    #template_name = 'yurjin_tour/contract_list.html'
    #context_object_name = 'latest_contract_list'
    
    #model = Contract
    queryset = Contract.objects.order_by('-input_date')

    #def get_queryset(self):
    #    Для фильтрации по пользователю - self.request.user
    #    self.manager = get_object_or_404(Manager, id=1)
    #    return Contract.objects.filter(manager = self.manager).order_by('-input_date')[:5]






#def ContractEditView(request,contract_id):
#    contract=Contract.objects.get(pk=contract_id)
#    form = ContractForm(instance=contract)
#    return render(request, 'yurjin_tour/contract_edit.html', {'form': form})


class ContractEditView(generic.UpdateView):
    #template_name = 'yurjin_tour/contract_edit.html'
    #form_class = ContractForm(object)
    
    #def get_form(self, form_class):
    #    return form_class(object)
    
    #contract=Contract.objects.get(pk=pk)
    #form = ContractForm(instance=contract)
    model = Contract
    #exclude = ('contract_id',)
    fields = ['contract_num','input_date', 'client']
    #localized_fields = "__all__"
    
    #form_class = ContractForm
    
    #def get_queryset(self):
    #    return Contract.objects.filter(input_date__lte=timezone.now())




class IndexView(generic.ListView):
    template_name = 'yurjin_tour/index.html'
    context_object_name = 'latest_contract_list'

    def get_queryset(self):
        return Contract.objects.filter(
            input_date__lte=timezone.now()
        ).order_by('-input_date')[:5]
        

class ContractDetailView(generic.DetailView):
    model = Contract
    template_name = 'yurjin_tour/contract_detail.html'
    
    def get_queryset(self):
        return Contract.objects.filter(input_date__lte=timezone.now())
    

def contract_save(request, contract_id):
    pass
