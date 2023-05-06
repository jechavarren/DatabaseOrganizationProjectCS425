from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import person_user

class CustomUserCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    

    class Meta:
        model = person_user
        fields = ('email', 'name')
