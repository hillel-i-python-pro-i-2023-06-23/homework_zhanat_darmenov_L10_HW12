# HW12/HW12/models/contact.py

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
