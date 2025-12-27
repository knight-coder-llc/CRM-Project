from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Accounts
    path('accounts/', views.AccountListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/', views.AccountDetailView.as_view(), name='account_detail'),
    path('accounts/create/', views.AccountCreateView.as_view(), name='account_create'),
    path('accounts/<int:pk>/update/', views.AccountUpdateView.as_view(), name='account_update'),
    
    # Contacts
    path('contacts/', views.ContactListView.as_view(), name='contact_list'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
    
    # Leads
    path('leads/', views.LeadListView.as_view(), name='lead_list'),
    path('leads/<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail'),
    path('leads/create/', views.LeadCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead_update'),
    
    # Opportunities
    path('opportunities/', views.OpportunityListView.as_view(), name='opportunity_list'),
    path('opportunities/<int:pk>/', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('opportunities/create/', views.OpportunityCreateView.as_view(), name='opportunity_create'),
    path('opportunities/<int:pk>/update/', views.OpportunityUpdateView.as_view(), name='opportunity_update'),
]
