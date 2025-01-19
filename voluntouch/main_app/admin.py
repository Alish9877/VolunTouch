from django.contrib import admin
from .models import Organization
from .models import Opportunity, Application

# Register your models here.
admin.site.register(Opportunity)
admin.site.register(Organization)
admin.site.register(Application)
