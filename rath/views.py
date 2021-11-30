from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'rath/home.html')


def index(request):
    return render(request, 'rath/index.html')


def menu_button(request):

    return render(request, 'rath/menu.html',)
