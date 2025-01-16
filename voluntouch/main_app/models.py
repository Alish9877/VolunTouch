from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    contactEmail = models.CharField(max_length=100)
    contactPhone = models.IntegerField()