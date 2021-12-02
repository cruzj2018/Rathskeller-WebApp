from django.shortcuts import render
from django.contrib.sessions.models import Session
from .models import Item, Category


def home(request):
    return render(request, "rath/home.html")


def index(request):
    categories = Category.objects.all()
    return render(request, "rath/index.html", {"categories": categories})


def menu_button(request):

    return render(
        request,
        "rath/menu.html",
    )
