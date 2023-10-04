# phonebook/services/contact_generation.py

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
