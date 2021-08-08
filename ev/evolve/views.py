from django.shortcuts import render

# Create your views here.
def home(response):
    return render (response, "evolve/index.html", {})


def about(response):
    return render (response, "evolve/about.html", {})


def services(response):
    return render (response, "evolve/services.html", {})


def contact(response):
    return render (response, "evolve/contact.html", {})