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

from common.views import FilteredAndSortedView

from django.template.context_processors import request
from django.contrib.messages.views import SuccessMessageMixin

from dal import autocomplete
from yurjin_tour.models import Office
from lib2to3.fixes.fix_input import context


class ProfileEditView(SuccessMessageMixin,generic.UpdateView):
    def get_object(self):
        return self.request.user.manager
        
    template_name = 'yurjin_tour/profile_edit.html'
    model = Manager
    form_class=forms.ProfileForm
    success_url = reverse_lazy('yurjin_tour:index')
    success_message = "Профиль успешно изменен"


class TouristList(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tourist.objects.all()

        if self.q:
            qs = qs.filter(last_name__istartswith=self.q)
            
        return qs


class ContractEditView(SuccessMessageMixin,generic.UpdateView):
    template_name = 'yurjin_tour/contract_edit.html'
    model = Contract
    form_class=forms.ContractForm
    success_url = reverse_lazy('yurjin_tour:index')
    success_message = "Договор успешно изменен"        

    def form_valid(self, form):
        form.instance.status = form.instance.get_contract_status()
        
        return super(ContractEditView, self).form_valid(form)


class ContractCreateView(SuccessMessageMixin,generic.CreateView):
    def get_num(self):
        #last_contract = Contract.objects.latest(field_name='contract_date')
        last_contract = Contract.objects.order_by('-contract_date','-contract_num')[0:1].get()
        if (last_contract.contract_date.year==timezone.datetime.today().year and last_contract.contract_date.month==timezone.datetime.today().month):
            new_num=last_contract.contract_num+1
        else:
            new_num=1
        return new_num

    def form_valid(self, form):
        form.instance.manager = self.request.user.manager
        form.instance.office = self.request.user.manager.office
        form.instance.signatory = self.request.user.manager.office.tour_agency.director
        form.instance.contract_num = self.get_num()
        form.instance.status = self.get_status()
        
        return super(ContractCreateView, self).form_valid(form)    
  
    template_name = 'yurjin_tour/contract_edit.html'
    model = Contract    
    initial = {
                'contract_date': timezone.datetime.today(),
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
    success_url = reverse_lazy('yurjin_tour:index')
    #success_message = "Договор успешно удален"
        

class ContractArchiveIndexView(generic.ArchiveIndexView):
    model = Contract
    date_field = 'contract_date'


class ContractYearArchiveView(generic.YearArchiveView):
    model = Contract
    date_field = 'contract_date'
    

class ContractList():
    def get_queryset(self):
        #qs = Tourist.objects.all()

        #if self.q:
        #    qs = qs.filter(last_name__istartswith=self.q)
            
        #return qs
        pass
    pass
    

class ContractMonthArchiveView(generic.MonthArchiveView,ContractList):
    model = Contract
    date_field = 'contract_date'
    month_format = '%m' 
    context_object_name = 'contract_list'
    #template_name = 'yurjin_tour/contract_list.html'



class ContractListView(FilteredAndSortedView, generic.ListView):
    #filter=None
    template_name = 'yurjin_tour/index.html'
    model = Contract
    paginate_by = 10
    #template_name = 'yurjin_tour/contract_list.html'
    #context_object_name = 'latest_contract_list'
    
    #model = Contract
    #queryset = Contract.objects.order_by('-contract_date')

    #def get_queryset(self):
    #    Для фильтрации по пользователю - self.request.user
    #    self.manager = get_object_or_404(Manager, id=1)
    #    return Contract.objects.filter(manager = self.manager).order_by('-input_date')[:5]    

    def get_queryset(self):
        q=Contract.objects.all()
        if (self.request.user.is_superuser):
            pass
        elif (self.request.user.manager == self.request.user.manager.office.tour_agency.director):
            q=q.filter(office__in=Office.objects.filter(tour_agency=self.request.user.manager.office.tour_agency))
        else:
            q=q.filter(office=self.request.user.manager.office)
        
        if (self.filter):
            q=q.filter(tourist_list__in=Tourist.objects.filter(last_name__icontains=self.filter)).distinct()

        #q=q.filter(office=self.request.user.manager.manager_office)
        
        #contract_date__lte=timezone.now()
        #filter=()
        #return Contract.objects.filter(manager=self.request.user.manager,contract_date__lte=timezone.now()).order_by('-contract_date','-contract_num')
        #return Contract.objects.filter(manager=self.request.user.manager,contract_date__lte=timezone.now()).order_by('-contract_date','-contract_num')
        return q.order_by('-contract_date','-contract_num')
    

class TouristListView(FilteredAndSortedView, generic.ListView):
    #template_name = 'yurjin_tour/tourist_list.html'
    model = Tourist
    paginate_by = 5
    
    def get_queryset(self):
        q = Tourist.objects.all()
        if (self.request.user.is_superuser):
            pass
        else:
            q = q.filter(office__in=Office.objects.filter(tour_agency=self.request.user.manager.office.tour_agency))
        if (self.filter):
            q = q.filter(last_name__icontains = self.filter)
        
        return q.order_by('last_name', 'first_name', 'mid_name')


class TouristEditView(SuccessMessageMixin,generic.UpdateView):
    template_name = 'yurjin_tour/tourist_edit.html'
    model = Tourist
    form_class=forms.TouristForm
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Данные туриста успешно изменены"        


class TouristCreateView(SuccessMessageMixin,generic.CreateView):    
    template_name = 'yurjin_tour/tourist_edit.html'
    model = Tourist
    form_class=forms.TouristForm
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Даннные туриста успешно добавлены"
    
    def form_valid(self, form):
        form.instance.office = self.request.user.manager.office
        
        return super(TouristCreateView, self).form_valid(form)         


class TouristDeleteView(generic.DeleteView):
    model = Tourist
    template_name = "yurjin_tour/tourist_delete.html"
    success_url = reverse_lazy('yurjin_tour:tourist_list')
    success_message = "Данные туриста успешно удалены"    
    
      
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
    





class ContractPdfPrint(generic.TemplateView): 
    template_name = "yurjin_tour/contract_print.html"

