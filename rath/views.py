from django.shortcuts import render
from .models import Item


# Create your views here.
def home(request):
    return render(request, "rath/home.html")


def index(request):
    items = Item.objects.all()
    return render(request, "rath/index.html", {"items": items})


def menu_button(request):

    return render(
        request,
        "rath/menu.html",
    )
