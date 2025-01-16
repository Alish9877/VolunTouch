from django.contrib import admin
from .models import Organization
from .models import Opportunity

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Organization)
