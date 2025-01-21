from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    
    path('organizations/', views.organization_index, name="index"),
    path('opportunities/update/<int:pk>/', views.OpportunityUpdate.as_view(), name='opportunity_update'),
    path('opportunities/delete/<int:pk>/', views.OpportunityDelete.as_view(), name='opportunity_delete'),
    path('opportunities/create/', views.opportunity_create, name='opportunity_create'),

    path('profile/', views.profile_index, name='index'),
    path('profile/edit/' , views.edit_profile, name='edit')
]