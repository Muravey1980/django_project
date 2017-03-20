from django.views.generic.base import TemplateView
from django.http import HttpResponse

def index(request):
    html_string="admin<br>polls<br>yurjin_tour"
    return HttpResponse(html_string)

class MainPageView(TemplateView):
    template_name = 'main_page.html' 
    
    