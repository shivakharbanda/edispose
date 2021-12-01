from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='edispose-home'),
    path('about/', views.about, name='edispose-about'),
    path('faq/', views.faq, name='edispose-faq'),
    path('contact/', views.contact, name='edispose-contact'),
    path('vendors/', views.vendor_list, name='edispose-Vendors'),
]
