# phonebook/management/commands/create_contacts.py
# Used by: >>> python manage.py create_contacts --amount 100

import logging
from django.core.management.base import BaseCommand  # , CommandError
from phonebook.models import Contact
from phonebook.services.contact_generation import generate_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many Contacts you want to generate?",
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        logger = logging.getLogger("django")

        queryset = Contact.objects.all()
        logger.info(f"Current amount of Contacts before: {queryset.count()}, Contacts: {queryset}")

        for person in generate_contacts(amount=amount):
            person.is_auto_generated = True
            person.save()

        # Refresh the queryset to get the updated count
        queryset = Contact.objects.all()

        logger.info(f"Current amount of Contacts after: {queryset.count()}, Contacts: {queryset}")
