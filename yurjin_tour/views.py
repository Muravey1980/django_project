#from django.shortcuts import render
from django.http import HttpResponse
from .models import Contract

# Create your views here.
def index(request):
<<<<<<< Upstream, based on django_project/master
    return HttpResponse("Hello, world. You're at the yurjin_tour index.")
=======
    latest_contract_list = Contract.objects.order_by('-input_date')[:5]
    output = ', '.join([str(q.contract_num) for q in latest_contract_list])
    return HttpResponse(output)
>>>>>>> 1a09349 just edit


def contract_detail(request, contract_id):
    return HttpResponse("You're looking at contract %s." % contract_id)