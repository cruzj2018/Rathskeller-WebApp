from django.urls import path

from rath.views import Home, MenuPage, Checkout, ReviewCart

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/', ReviewCart.as_view(), name='cart'),
    path('menu/', MenuPage.as_view(), name="menu"),
    path('menu/checkout/', Checkout.as_view(), name="checkout")
]
