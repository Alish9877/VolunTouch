from django.shortcuts import render , redirect
from .forms import SignUpForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Organization
from .models import Opportunity
from .forms import OpportunityForm
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid signup - please try again later.'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("<h1>About the cat collector</h1>")
    return render(request, 'about.html')

def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'opportunity/list.html', {'opportunities': opportunities})

def opportunity_create(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')
    else:
        form = OpportunityForm()
    return render(request, 'opportunity/create.html', {'form': form})

def organization_index(request):
    Organizations = Organization.objects.all()
    return render(request, "organizations/index.html", {"organizations": Organizations})



class OpportunityUpdate(UpdateView):
    model = Opportunity
    fields = ['title', 'description','location', 'start_date', 'end_date', 'requirements']
    success_url = '/opportunities/'


class OpportunityDelete(DeleteView):
    model = Opportunity
    
    success_url = '/opportunities/'