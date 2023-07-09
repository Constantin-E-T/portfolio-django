# about/models

from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    testimonial = models.TextField()

    def __str__(self):
        return self.name
