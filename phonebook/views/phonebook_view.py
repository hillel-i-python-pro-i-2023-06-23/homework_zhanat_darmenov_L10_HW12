# phonebook/views/phonebook_view.py

from django.shortcuts import render  # , redirect
from phonebook.services.contact_management import generate_contacts, save_contacts, get_all_contacts

# from django.http import HttpResponse
# from phonebook.models import Contact


def home_page(request):
    if request.method == "POST":
        if request.POST.get("action") == "Generate":
            amount = int(request.POST.get("amount"))
            generated_contacts = list(generate_contacts(amount))
            save_contacts(generated_contacts)
            # Show only newly generated Contacts:
            return render(request, "contact_list.html", {"contacts": generated_contacts})

        if request.POST.get("action") == "Show All":
            return render(request, "contact_list.html", {"contacts": get_all_contacts()})

    return render(request, "home_page.html")
