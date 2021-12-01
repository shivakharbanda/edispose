from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Edispose\home.html', {'title' : 'Home'})

def about(request):
    return render(request, 'Edispose\\about.html', {'title' : 'About'})

def faq(request):
    return render(request, 'Edispose\\FAQ.html', {'title' : 'FAQ'})


def contact(request):
    return render(request, 'Edispose\\contact.html', {'title' : 'Contact'})

def vendor_list(request):
    return render(request, 'Edispose\\vendor_list.html')