from django.shortcuts import render
from .models import Opportunity
# Create your views here.


def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'opportunity/list.html', {'opportunities': opportunities})

def home(request):
    return render(request, 'base.html')