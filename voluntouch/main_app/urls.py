from django.urls import path
from . import views
urlpatterns = [
        path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', views.login, name='login')
    path('about/', views.about, name='about')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
]