# phonebook/management/commands/create_contacts.py
# Used by: >>> python manage.py create_contacts --amount 100

import logging
from django.core.management.base import BaseCommand  # , CommandError

# from phonebook.models import Contact
from phonebook.services import contact_management


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

        queryset = contact_management.get_all_contacts()
        logger.info(f"Current amount of Contacts before: {queryset.count()}, Contacts: {queryset}")

        # Go to phonebook/services/contact_generation.py: generate_contacts()
        # for person in generate_contacts(amount=amount):
        #     person.is_auto_generated = True
        #     person.save()

        contacts = contact_management.generate_contacts(amount=amount)

        contact_management.save_contacts(contacts=contacts)

        # Refresh the queryset to get the updated count
        queryset = contact_management.get_all_contacts()

        logger.info(f"Current amount of Contacts after: {queryset.count()}, Contacts: {queryset}")
