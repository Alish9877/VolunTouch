from django.urls import path
from . import views
urlpatterns = [
        path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', views.login, name='login')
    path('about/', views.about, name='about'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunities/create/', views.opportunity_create, name='opportunity_create'),
    path('organizations/', views.organization_index, name="index"),
    path('opportunities/update/<int:pk>/', views.OpportunityUpdate.as_view(), name='opportunity_update'),

]