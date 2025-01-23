from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', views.login, name='login'),
    path('about/', views.about, name='about'),

    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunities/update/<int:pk>/', views.OpportunityUpdate.as_view(), name='opportunity_update'),
    path('opportunities/delete/<int:pk>/', views.OpportunityDelete.as_view(), name='opportunity_delete'),
    path('opportunities/create/', views.opportunity_create, name='opportunity_create'),


    path('applications/', views.volunteer_applications, name='volunteer_applications'),
    path('apply/<int:opportunity_id>/', views.apply_for_opportunity, name='apply_for_opportunity'),
    path('applications/delete/<int:pk>/', views.ApplicationDelete.as_view(), name='application_delete'),
    path('view_applications/<int:opportunity_id>/', views.view_applications, name='view_applications'),
    path('application/<int:application_id>/', views.view_application, name='view_application'),
    path('change_status/<int:application_id>/', views.change_status, name='change_status'),


    path('profile/', views.profile_index, name='profile'),
    path('profile/edit/' , views.edit_profile, name='edit'),

    path('dashboard/', views.organization_dashboard, name='organization_dashboard'),
    path('organization/<int:organization_id>/', views.organization_detail, name='organization_detail'),

]