# services/views.py

from django.shortcuts import render
from .models import Service, Pricing
from about.models import Testimonial


def services(request):
    services = Service.objects.all()
    pricings = Pricing.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'services/services.html', {'services': services, 'testimonials': testimonials, 'pricings': pricings})
