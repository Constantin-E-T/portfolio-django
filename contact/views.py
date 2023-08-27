# contact/views.py

from django.shortcuts import render
from services.models import Pricing
from decimal import Decimal

def contact(request):
    pricings = Pricing.objects.all()
    selected_package = request.GET.get('package', '')
    
    for pricing in pricings:
        if pricing.discount:
            discount_factor = Decimal(pricing.discount) / 100
            pricing.discounted_price = pricing.price * (1 - discount_factor)
        else:
            pricing.discounted_price = pricing.price
    
    initial_data = {}
    if request.user.is_authenticated:
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone_number,
            'location': user.address,
            'postcode': user.postcode,
            'town': user.town,
            'country_of_residence': user.country_of_residence,
        }
    
    return render(request, 'contact/contact.html', {
        'selected_package': selected_package,
        'pricings': pricings,
        'initial_data': initial_data,
    })
