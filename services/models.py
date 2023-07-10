# services/models.py

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Pricing(models.Model):
    PACKAGE_CHOICES = (
        ('Basic', 'Basic'),
        ('Professional', 'Professional'),
        ('Business', 'Business'),
    )
    
    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    service1 = models.CharField(max_length=100)
    service2 = models.CharField(max_length=100)
    service3 = models.CharField(max_length=100)
    discount = models.IntegerField(null=True, blank=True)  # Discount in percentage
    

    def __str__(self):
        return self.package_type
