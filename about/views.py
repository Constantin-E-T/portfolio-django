# about/views.py

from django.shortcuts import render
from .models import Testimonial

def about(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'about/about.html', {'testimonials': testimonials})

