# phonebook/management/commands/delete_contacts.py
# >>> python manage.py delete_contacts --is-only-auto-generated

import logging
from django.core.management.base import BaseCommand
from phonebook.services import contact_management


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-auto-generated",
            help="Delete only auto generated Contacts",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        logger = logging.getLogger("django")
        queryset = contact_management.get_all_contacts()
        logger.info(f"Current amount of Contacts before: {queryset.count()}")

        logger.info("Delete only auto generated Contacts")

        if is_only_auto_generated:
            total_deleted, details = contact_management.delete_all_contacts()

        logger.info(f"Total deleted: {total_deleted}, details: {details}")
        logger.info(f"Current amount of Contacts after: {queryset.count()}")
