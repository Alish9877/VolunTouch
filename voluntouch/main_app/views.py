from django.shortcuts import render , redirect
from .forms import SignUpForm
from django.contrib.auth import login
from .models import Organization
from .models import Opportunity
from .forms import OpportunityForm
from .forms import ProfileForm
from django.views.generic.edit import UpdateView, DeleteView
from .models import Profile



# Create your views here.

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


def profile_index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile/index.html", {"profile": profile})



def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    print("profile", profile)
    print("request.method", request.method)

    if request.method == 'POST':
        print("here")
        form = ProfileForm(request.POST, instance=profile)
        print("form", form)

        if form.is_valid():
            profile.user_id = request.user.id
            form.save()
            return redirect('profile') 
    else:
        print("else")
        form = ProfileForm(instance=profile)
    return render(request, 'profile/edit.html', {'form': form})
    
def organization_list(request):
    organizations = Organization.objects.get(user=request.user)
    return render(request, "proforganizationsile/list.html", {"organizations": organizations})