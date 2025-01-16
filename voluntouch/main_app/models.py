from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    AppDate = models.DateField()
    Status = models.CharField(max_length=20)