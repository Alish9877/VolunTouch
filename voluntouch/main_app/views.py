from django.shortcuts import render, redirect , get_object_or_404
from .forms import SignUpForm
from django.contrib.auth import login
from django.http import Http404
from .models import Organization, Opportunity, Application, Profile
from .forms import OpportunityForm
from .forms import ProfileForm , ApplicationStatusForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
class OrganizationCreate(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'location', 'description', 'contactEmail', 'contactPhone']
    success_url = '/organizations/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
class OrganizationUpdate(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ['location', 'description', 'contactEmail', 'contactPhone']
    success_url = '/organizations/'


@login_required
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
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid signup - please try again later.'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def opportunity_list(request):
    if request.user.profile.user_type == 'volunteer':
        applied_opportunities = Application.objects.filter(user=request.user).values_list('opportunity', flat=True)
        opportunities = Opportunity.objects.exclude(id__in=applied_opportunities)
    elif request.user.profile.user_type == 'organization':
        organization = request.user.profile.organization
        if organization: 
            opportunities = Opportunity.objects.filter(organization=organization)
    else:
        opportunities = Opportunity.objects.all()
    return render(request, 'opportunity/list.html', {'opportunities': opportunities})


@login_required
def opportunity_create(request):
    if request.method == "POST":
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            if request.user.profile.user_type == 'organization':
                organization = request.user.profile.organization
                if organization:
                    opportunity.organization = organization
                    opportunity.save()
                    return redirect('opportunity_list')
                else:
                    form.add_error(None, "No organization associated with your profile.")
            else:
                form.add_error(None, "Only organizations can create opportunities.")
    else:
        form = OpportunityForm()

    return render(request, 'opportunity/create.html', {'form': form})



@login_required
def apply_for_opportunity(request, opportunity_id):
    try:
        opportunity = Opportunity.objects.get(id=opportunity_id)
    except Opportunity.DoesNotExist:
        raise Http404("Opportunity does not exist")
    Application.objects.create(
        user=request.user,
        opportunity=opportunity,
        AppDate=datetime.now()
    )
    return render(request, 'opportunity/detail.html', {'opportunity': opportunity})


@login_required
def volunteer_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'application/volunteer_applications.html', {'applications': applications})



class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = '/applications/'
    

class OpportunityUpdate(UpdateView):
    model = Opportunity
    fields = ['title', 'description', 'location', 'start_date', 'end_date', 'requirements']
    success_url = '/opportunities/'



class OpportunityDelete(DeleteView):
    model = Opportunity
    success_url = '/opportunities/'


@login_required
def profile_index(request):
    profile = Profile.objects.get(user=request.user)
    print("profile", profile)
    return render(request, "profile/index.html", {"profile": profile})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    print("profile", profile)
    print("request.method", request.method)
    if request.method == 'POST':
        print("here")
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        print("form", form)
        if form.is_valid():
            profile.user_id = request.user.id
            form.save()
            return redirect('profile') 
    else:
        print("else")
        form = ProfileForm(instance=profile)
    return render(request, 'profile/edit.html', {'form': form})


@login_required
def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    return render(request, 'organizations/detail.html', {'organization': organization})


@login_required
def organization_dashboard(request):
    if request.user.profile.user_type != 'organization':
        return redirect('home')
    opportunities = Opportunity.objects.filter(organization__profile__user=request.user)
    return render(request, 'organizations/organization_dashboard.html', {'opportunities': opportunities})


@login_required
def change_status(request, application_id):
    if request.user.profile.user_type != 'organization':
        return redirect('home') 
    application = get_object_or_404(Application, id=application_id)
    if application.opportunity.organization.profile.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('view_applications', opportunity_id=application.opportunity.id)
    else:
        form = ApplicationStatusForm(instance=application)
    return render(request, 'application/change_status.html', {'form': form, 'application': application})


@login_required
def view_applications(request, opportunity_id):
    if request.user.profile.user_type != 'organization':
        return redirect('home')
    opportunity = get_object_or_404(Opportunity, id=opportunity_id)
    if opportunity.organization.profile.user != request.user:
        return redirect('home') 
    applications = Application.objects.filter(opportunity=opportunity)
    return render(request, 'application/view_applications.html', {'applications': applications, 'opportunity': opportunity})

@login_required
def view_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('organization_dashboard') 
    else:
        form = ApplicationStatusForm(instance=application)
    return render(request, 'application/view_application.html', {'application': application,'form': form,})