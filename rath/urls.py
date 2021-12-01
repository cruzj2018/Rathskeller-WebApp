from django.urls import path
from . import views

app_name = "rath"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('menu_button', views.menu_button, name="menu_button")
]
