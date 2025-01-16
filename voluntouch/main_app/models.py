from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField()

    def __str__(self):
        return self.titleclass Application(models.Model):
    AppDate = models.DateField()
    Status = models.CharField(max_length=20)