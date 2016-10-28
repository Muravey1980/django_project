#from django.shortcuts import render
from django.http import HttpResponse
from .models import Contract

# Create your views here.
def index(request):
    latest_contract_list = Contract.objects.order_by('-input_date')[:5]
    output = ', '.join([str(q.contract_num) for q in latest_contract_list])
    return HttpResponse(output)


def contract_detail(request, contract_id):
    return HttpResponse("You're looking at contract %s." % contract_id)