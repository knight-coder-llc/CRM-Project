from django.test import TestCase
from django.urls import reverse
from .models import Account, Contact, Lead, Opportunity

class ViewTests(TestCase):
    def setUp(self):
        # Create some data for detail views
        self.account = Account.objects.create(name="Test Account")
        self.contact = Contact.objects.create(account=self.account, first_name="John", email="john@example.com")
        self.lead = Lead.objects.create(first_name="Jane", email="jane@example.com")
        self.opportunity = Opportunity.objects.create(account=self.account, name="Test Deal", amount=100, close_date="2024-01-01")

    def test_dashboard_status(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_account_list_status(self):
        response = self.client.get(reverse('account_list'))
        self.assertEqual(response.status_code, 200)

    def test_account_detail_status(self):
        response = self.client.get(reverse('account_detail', args=[self.account.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_list_status(self):
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)

    def test_lead_list_status(self):
        response = self.client.get(reverse('lead_list'))
        self.assertEqual(response.status_code, 200)

    def test_opportunity_list_status(self):
        response = self.client.get(reverse('opportunity_list'))
        self.assertEqual(response.status_code, 200)
