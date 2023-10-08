# phonebook/services/contact_management.py

from collections.abc import Iterator
from faker import Faker
from phonebook.models import Contact

faker = Faker()


def generate_contact() -> Contact:
    return Contact(
        name=faker.first_name(),
        phone=faker.phone_number(),
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()


def save_contacts(contacts):
    for person in contacts:
        person.is_auto_generated = True
        person.save()


def get_all_contacts():
    return Contact.objects.all()
