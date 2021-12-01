from django.contrib import admin
from .models import User, Vendor
# Register your models here.
admin.site.register(User)
admin.site.register(Vendor)

list_display = [field.name for field in User._meta.get_fields()]