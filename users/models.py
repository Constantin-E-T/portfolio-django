# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Existing fields
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    # New fields
    DoB = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    postcode = models.CharField(max_length=10, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    country_of_residence = models.CharField(max_length=255, null=True, blank=True)

    # Note: AbstractUser already includes fields for first_name and last_name, 
    # so you don't need to add them again.
