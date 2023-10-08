# phonebook/views/phonebook_view.py

from django.shortcuts import render  # , redirect

# from django.http import HttpResponse
from phonebook.services.contact_management import generate_contacts, save_contacts  # , get_all_contacts

# from phonebook.models import Contact


def home_page(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        generated_contacts = list(generate_contacts(amount))
        save_contacts(generated_contacts)
        # Show only newly generated Contacts:
        return render(request, "contact_list.html", {"contacts": generated_contacts})

        # Add "Show All Contacts" Button:

    return render(request, "home_page.html")
