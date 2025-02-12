from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Opportunity
from .models import Profile
from .models import Application


class SignUpForm(UserCreationForm):
    VOLUNTEER = 'volunteer'
    ORGANIZATION = 'organization'
    USER_TYPE_CHOICES = [
        (VOLUNTEER, 'Volunteer'),
        (ORGANIZATION, 'Organization'),
    ]
    
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect , required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2' , 'user_type'] 



class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'requirements', 'organization']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio', 'location' , 'skills' , 'interests' ]


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['Status']