from django.shortcuts import render , redirect
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from .models import Organization
from .models import Opportunity
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class OrganizationCreate(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'location', 'description', 'contactEmail', 'contactPhone']

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

    return render(request, 'about.html')


def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'opportunity/list.html', {'opportunities': opportunities})


def organization_index(request):
    Organizations = Organization.objects.all()
    return render(request, "organizations/index.html", {"organizations": Organizations})