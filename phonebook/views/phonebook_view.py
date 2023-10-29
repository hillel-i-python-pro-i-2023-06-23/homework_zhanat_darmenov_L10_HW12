# phonebook/views/phonebook_view.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from phonebook.models import Contact
from phonebook.services.contact_management import (
    generate_contacts,
    save_contacts,
    get_all_contacts,
    delete_all_contacts,
    delete_contact,
)


def home_page(request):
    if request.method == "POST":
        if request.POST.get("action") == "Generate":
            amount = int(request.POST.get("amount"))
            return redirect(reverse("contact_list") + f"?amount={amount}")

    return render(request, "home_page.html")


def contact_list(request):
    amount = request.GET.get("amount", 0)
    amount = int(amount)

    if request.method == "POST":
        if request.POST.get("action") == "Show All":
            return render(request, "contact_list.html", {"contacts": get_all_contacts()})

        elif request.POST.get("action") == "Return":
            return redirect(home_page)

        elif request.POST.get("action") == "Delete All":
            delete_all_contacts()
            return render(request, "contact_list.html", {"contacts": get_all_contacts()})

    # Generate, save & show only new Contacts:
    generated_contacts = list(generate_contacts(amount))
    save_contacts(generated_contacts)
    return render(request, "contact_list.html", {"contacts": generated_contacts})


# def delete_contacts(request):
#     if request.method == "POST":
#         if request.POST.get("action") == "Show All":
#             return redirect(reverse("contact_list"))
#
#         elif request.POST.get("action") == "Delete All":
#             delete_all_contacts()
#             return render(request, "contact_list.html", {"contacts": get_all_contacts()})
#
#         elif request.POST.get("action") == "Return":
#             return redirect(home_page)
#     return render(request, "contact_list.html")


def show_single_user(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    print(f"{type(contact)} !!!!!!!!!!!!!!!!!!!!!!!!!!! type")

    if request.method == "POST":
        if request.POST.get("action") == "Change Info":
            return redirect(reverse("alter_user", args=[contact_id]))
            # return render(request, "alter_user.html", {"contact": contact})

        elif request.POST.get("action") == "Delete Contact":
            delete_contact(contact_id)
            return redirect(reverse("contact_list"))

        elif request.POST.get("action") == "Return to Start":
            return redirect(home_page)

    return render(request, "single_user.html", {"contact": contact})


def alter_user(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        if request.POST.get("action") == "Submit Info":
            contact.name = request.POST.get("name")
            contact.phone = request.POST.get("phone")
            contact.save()
            return redirect(reverse("single_user", args=[contact_id]))

        elif request.POST.get("action") == "Return to Start":
            return redirect("home_page")

    return render(request, "alter_user.html", {"contact": contact})
