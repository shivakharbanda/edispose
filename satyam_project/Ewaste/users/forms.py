from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Vendor

User = get_user_model()

class CitizenRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_citizen = True
        if commit:
            user.save()
        return user


class VendorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField(max_length=1000)
    phone_number = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['username', 'email','address','phone_number', 'password1', 'password2']

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        
        if commit:
            user.save()
        return user