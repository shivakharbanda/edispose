from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CitizenRegisterForm, VendorRegisterForm
from .models import Vendor

from django.contrib.auth import get_user_model

User = get_user_model()

def register_citizen(request):
    model = User
    if request.method == 'POST':
        form = CitizenRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You are now able to login")
            return redirect('login')
    else:
        form = CitizenRegisterForm()
    
    return render(request, 'users/register_citizen.html', {'form': form})



def register_vendor(request):
    model = Vendor
    if request.method == 'POST':
        form = VendorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            address = form.cleaned_data.get('address')
            messages.success(request, f"Your account has been created! You are now able to login")
            return redirect('login')

    else:
        form = VendorRegisterForm()
    return render(request, 'users/register_vendor.html', {'form': form})