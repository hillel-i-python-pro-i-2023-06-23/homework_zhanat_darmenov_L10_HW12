# phonebook/models/contact.py

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    creation_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    alteration_date = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    # Magic method to represent the object as a unique string.
    # Used for Debug:
    __repr__ = __str__
