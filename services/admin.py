# services/admin.py

from django.contrib import admin
from .models import Service, Pricing

admin.site.register(Service)
admin.site.register(Pricing)