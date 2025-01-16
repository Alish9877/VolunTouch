from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

from .models import Opportunity
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid signup - please try again later.'
    form = CustomUserCreationForm()
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

def home(request):
    return render(request, 'base.html')