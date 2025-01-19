from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Opportunity
from .models import Profile


class SignUpForm(forms.ModelForm):
    VOLUNTEER = 'volunteer'
    ORGANIZATION = 'organization'
    USER_TYPE_CHOICES = [
        (VOLUNTEER, 'Volunteer'),
        (ORGANIZATION, 'Organization'),
    ]
    
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        return user
