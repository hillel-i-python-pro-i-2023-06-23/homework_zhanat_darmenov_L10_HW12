# phonebook/models/contact.py

from django.db import models


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )
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

    # This class is used to define metadata options for the model.
    class Meta:
        ordering = ["alteration_date", "name"]
