from django.shortcuts import render
from .models import Organization
# Create your views here.

def organization_index(request):

    Organizations = Organization.objects.all()

    return render(request, "organizations/index.html", {"organizations": Organizations})