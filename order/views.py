from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from rath.models import Item, ItemAttribute
from .models import OrderItem
from .cart import Cart

# Create your views here.


def order_list(request):
    ordered_items = OrderItem.objects.all()
    return render(request, "order/order_items.html", {"ordered_items": ordered_items})


def add_item(request):
    if request.method == "POST":
        cart = Cart(request)
        if request.htmx:
            item_id = request.POST.get("item-id")
            quantity = request.POST.get("total")
            selected = request.POST.getlist("selected")
            item = Item.objects.get(id=item_id)
            if selected:
                extra = item.item_attributes.filter(id__in=selected).values()
                cart.add(product=item, quantity=int(quantity), extra=extra)
                return render(request, "rath/partials/success.html", {"item": item})
            else:
                cart = cart.add(product=item, quantity=int(quantity))
                return render(request, "rath/partials/success.html", {"item": item})
    else:
        return JsonResponse({"data": "Error"}, status=403)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.add_message(request, messages.INFO, "Order cleared!")
    # messages.add_message(request, messages.INFO, 'Hello world.')
    return redirect("order:order-list")


def order_create(request):
    if request.method == "POST":

        if request.htmx:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            address = request.POST.get("address")


    return JsonResponse({"created": "created"}, status=203)