from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    contactEmail = models.CharField(max_length=100)
    contactPhone = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField()

    def __str__(self):
        return self.title
    