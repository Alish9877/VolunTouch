from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/login/', views.login, name='login')
    path('about/', views.about, name='about'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('organizations/', views.organization_index, name="index"),
    path('organizations/create/', views.OrganizationCreate.as_view(), name='organizations_create'),
    path('organizations/<int:pk>/update/', views.OrganizationUpdate.as_view(), name='organizations_update'),
    path('organizations/<int:pk>/delete/', views.OrganizationDelete.as_view(), name='organizations_delete'),
]