'''
Created on 2017-03-20
@author:   067SvobodskiiSE
@contact: ssvobodskii@067.pfr.ru
'''
from django.views.generic.base import View

class FilteredAndSortedView(View):
    def get(self, request, *args, **kwargs):
        try:
            self.filter = self.request.GET['filter']
        except KeyError:
            self.filter = ""
        
        return super(FilteredAndSortedView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(FilteredAndSortedView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context