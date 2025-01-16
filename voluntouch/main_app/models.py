from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    contactEmail = models.EmailField(max_length=100)
    contactPhone = models.CharField(max_length=20) 

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    AppDate = models.DateField()
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application for {self.opportunity.title} by {self.user.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    location = models.CharField(max_length=100) 
    skills = models.TextField(max_length=300)
    interests = models.TextField(max_length=300) 

    def __str__(self):
        return f"{self.user.username}'s Profile"
