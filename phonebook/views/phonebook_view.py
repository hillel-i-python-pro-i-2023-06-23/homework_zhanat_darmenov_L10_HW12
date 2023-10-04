# phonebook/views/phonebook_view.py

from django.shortcuts import render  # , redirect

# from django.http import HttpResponse
from phonebook.services.contact_generation import generate_contacts

# from phonebook.models import Contact


def home_page(request):
    if request.method == "POST":
        # Handle the form submission here
        try:
            amount = int(request.POST.get("amount"))
            generated_contacts = list(generate_contacts(amount))
            # Do something with the generated_contacts, such as saving them to the database.
            return render(request, "contact_list.html", {"contacts": generated_contacts})
        except ValueError:
            # Handle invalid input (e.g., non-integer value)
            error_message = "Please enter a valid number."
            return render(request, "contact_list.html", {"error_message": error_message})

    return render(request, "home_page.html")
