from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.


def home(request):
    return render(request, 'rath/home.html')


def menu_button(request):
    menu = Menu.objects.all()
    return render(request, 'rath/menu.html', {'menu': menu})
