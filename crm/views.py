from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum, Count
from .models import Account, Contact, Lead, Opportunity

class DashboardView(TemplateView):
    template_name = 'crm/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_accounts'] = Account.objects.count()
        context['total_contacts'] = Contact.objects.count()
        context['total_leads'] = Lead.objects.count()
        context['total_opportunities'] = Opportunity.objects.count()
        
        # Simple pipeline summary
        context['pipeline_value'] = Opportunity.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        context['recent_leads'] = Lead.objects.order_by('-created_at')[:5]
        return context

# --- Account Views ---
class AccountListView(ListView):
    model = Account
    template_name = 'crm/account_list.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'crm/account_detail.html'
    context_object_name = 'account'

class AccountCreateView(CreateView):
    model = Account
    template_name = 'crm/account_form.html'
    fields = '__all__'
    success_url = reverse_lazy('account_list')

class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'crm/account_form.html'
    fields = '__all__'
    success_url = reverse_lazy('account_list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'crm/account_confirm_delete.html'
    success_url = reverse_lazy('account_list')

# --- Contact Views ---
class ContactListView(ListView):
    model = Contact
    template_name = 'crm/contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'crm/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'crm/contact_form.html'
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'crm/contact_form.html'
    fields = '__all__'
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'crm/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')

# --- Lead Views ---
class LeadListView(ListView):
    model = Lead
    template_name = 'crm/lead_list.html'
    context_object_name = 'leads'

class LeadDetailView(DetailView):
    model = Lead
    template_name = 'crm/lead_detail.html'
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    model = Lead
    template_name = 'crm/lead_form.html'
    fields = '__all__'
    success_url = reverse_lazy('lead_list')

class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'crm/lead_form.html'
    fields = '__all__'
    success_url = reverse_lazy('lead_list')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'crm/lead_confirm_delete.html'
    success_url = reverse_lazy('lead_list')

# --- Opportunity Views ---
class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'crm/opportunity_list.html'
    context_object_name = 'opportunities'

class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'crm/opportunity_detail.html'
    context_object_name = 'opportunity'

class OpportunityCreateView(CreateView):
    model = Opportunity
    template_name = 'crm/opportunity_form.html'
    fields = '__all__'
    success_url = reverse_lazy('opportunity_list')

class OpportunityUpdateView(UpdateView):
    model = Opportunity
    template_name = 'crm/opportunity_form.html'
    fields = '__all__'
    success_url = reverse_lazy('opportunity_list')

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    template_name = 'crm/opportunity_confirm_delete.html'
    success_url = reverse_lazy('opportunity_list')

class DocumentationView(TemplateView):
    template_name = 'crm/documentation.html'
