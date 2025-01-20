from django.shortcuts import render , redirect
from .forms import SignUpForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Organization
from .models import Opportunity
from .forms import OpportunityForm
from django.views.generic.edit import UpdateView, DeleteView
from .models import Profile



from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class OrganizationCreate(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'location', 'description', 'contactEmail', 'contactPhone']
    success_url = '/organizations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrganizationUpdate(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ['location', 'description', 'contactEmail', 'contactPhone']
    success_url = '/organizations/'

class OrganizationDelete(LoginRequiredMixin, DeleteView):
    model = Organization
    success_url = '/organizations/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            Profile.objects.create(user=user, user_type=user_type) 
            
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

    return render(request, 'about.html')


def opportunity_list(request):
    if request.user.profile.user_type == 'organization':
        opportunities = Opportunity.objects.filter(organization=request.user)  
    else:
        opportunities = Opportunity.objects.all()
    return render(request, 'opportunity/list.html', {'opportunities': opportunities})

def opportunity_create(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            opportunity.organization = request.user 
            opportunity.save()  
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