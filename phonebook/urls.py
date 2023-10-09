"""
URL configuration for phonebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phonebook.views.phonebook_view import home_page, contact_list, delete_contacts, show_single_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home_page"),
    path("contacts/", contact_list, name="contact_list"),
    path("contacts/delete/", delete_contacts, name="delete_contacts"),
    path("contacts/single-user/<int:contact_id>/", show_single_user, name="single_user"),
]
