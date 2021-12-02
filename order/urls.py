from django.urls import path
from . import views
app_name = "order"

urlpatterns = [
    path("my-order/", views.order_list, name="order-list"),
    path("order/add/", views.add_item, name="add"),
    path("cart/clear/", views.clear_cart, name="clear-cart"),
]