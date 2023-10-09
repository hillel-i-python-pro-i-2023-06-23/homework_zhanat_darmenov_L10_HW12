# phonebook/views/phonebook_view.py

from django.shortcuts import render, redirect
from django.urls import reverse
from phonebook.services.contact_management import (
    generate_contacts,
    save_contacts,
    get_all_contacts,
    delete_all_contacts,
)


def home_page(request):
    if request.method == "POST":
        if request.POST.get("action") == "Generate":
            amount = int(request.POST.get("amount"))
            return redirect(reverse("contact_list") + f"?amount={amount}")

    return render(request, "home_page.html")


def contact_list(request):
    amount = request.GET.get("amount", 1)  # Default: 1
    amount = int(amount)

    if request.method == "POST":
        if request.POST.get("action") == "Show All":
            return render(request, "contact_list.html", {"contacts": get_all_contacts()})
        if request.POST.get("action") == "Return":
            return redirect(home_page)
        if request.POST.get("action") == "Delete All":
            return redirect(reverse("delete_contacts"))

    # Generate, save & show only new Contacts:
    generated_contacts = list(generate_contacts(amount))
    save_contacts(generated_contacts)
    return render(request, "contact_list.html", {"contacts": generated_contacts})


def delete_contacts(request):
    if request.method == "POST":
        if request.POST.get("action") == "Delete All":
            delete_all_contacts()
            return render(request, "contact_list.html", {"contacts": get_all_contacts()})
        if request.POST.get("action") == "Return":
            return redirect(home_page)
    return render(request, "contact_list.html")
