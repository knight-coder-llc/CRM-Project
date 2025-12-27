from django.core.management.base import BaseCommand
from crm.models import Account, Contact, Lead, Opportunity
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Account.objects.all().delete()
        Contact.objects.all().delete()
        Lead.objects.all().delete()
        Opportunity.objects.all().delete()

        self.stdout.write('Creating Accounts...')
        accounts = []
        industries = ['tech', 'finance', 'health', 'retail']
        for i in range(5):
            acc = Account.objects.create(
                name=f'Company {i+1}',
                industry=random.choice(industries),
                website=f'https://company{i+1}.com',
                phone=f'555-010{i}',
                address=f'{i+1} Business Way, Tech City'
            )
            accounts.append(acc)

        self.stdout.write('Creating Contacts...')
        for acc in accounts:
            for i in range(3):
                Contact.objects.create(
                    account=acc,
                    first_name=f'Contact{acc.id}',
                    last_name=f'User{i}',
                    email=f'user{i}@company{acc.id}.com',
                    phone=f'555-020{i}',
                    role='Manager' if i == 0 else 'Employee'
                )

        self.stdout.write('Creating Leads...')
        statuses = ['new', 'contacted', 'qualified', 'lost']
        for i in range(10):
            Lead.objects.create(
                first_name=f'Lead',
                last_name=f'Prospect{i}',
                email=f'lead{i}@example.com',
                company=f'Startup {i}',
                status=random.choice(statuses),
                source='web'
            )

        self.stdout.write('Creating Opportunities...')
        stages = ['prospecting', 'negotiation', 'closed_won', 'closed_lost']
        for acc in accounts:
            for i in range(2):
                Opportunity.objects.create(
                    account=acc,
                    name=f'Deal {acc.name} - {i+1}',
                    amount=random.randint(1000, 50000),
                    stage=random.choice(stages),
                    close_date=timezone.now().date() + timedelta(days=random.randint(10, 60))
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
