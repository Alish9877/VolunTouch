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

    path('organizations/create/', views.OrganizationCreate.as_view(), name='organizations_create'),
    path('organizations/<int:pk>/update/', views.OrganizationUpdate.as_view(), name='organizations_update'),
    path('organizations/<int:pk>/delete/', views.OrganizationDelete.as_view(), name='organizations_delete'),
    path('apply/<int:opportunity_id>/', views.apply_for_opportunity, name='apply_for_opportunity'),
]