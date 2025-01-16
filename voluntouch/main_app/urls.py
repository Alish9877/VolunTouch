from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
]