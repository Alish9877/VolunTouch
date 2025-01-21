from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    contactEmail = models.CharField(max_length=100)
    contactPhone = models.IntegerField()
    def __str__(self):
        return self.name

class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField()
    organization = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='opportunities'
    )
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
    VOLUNTEER = 'volunteer'
    ORGANIZATION = 'organization'
    USER_TYPE_CHOICES = [
        (VOLUNTEER, 'Volunteer'),
        (ORGANIZATION, 'Organization'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=VOLUNTEER,
    )
    bio = models.TextField(max_length=300)
    location = models.CharField(max_length=100)
    skills = models.TextField(max_length=300)
    interests = models.TextField(max_length=300)
    def __str__(self):
        return f"{self.user.username}'s Profile"
