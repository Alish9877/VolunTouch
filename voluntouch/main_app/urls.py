from django.urls import path
from . import views

urlpatterns = [

    path('organizations/', views.organization_index, name="index"),

]