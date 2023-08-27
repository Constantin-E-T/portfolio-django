# portfolio/views.py

from django.shortcuts import render

def contact_page(request):
    context = {
        'EMAILJS_USER': config('EMAILJS_USER')
    }
    return render(request, 'contact/contact.html', context)
