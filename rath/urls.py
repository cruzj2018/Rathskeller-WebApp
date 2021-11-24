from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu_button', views.menu_button, name="menu_button")
]
