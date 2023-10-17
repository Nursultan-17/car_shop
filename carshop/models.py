from django.db import models
from django.contrib.auth.models import User



class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    engine_capacity = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
