from django.shortcuts import render, get_object_or_404
from django.contrib.sessions.models import Session
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
                attrs = item.item_attributes.filter(id__in=selected)
                cart.add(product=item, quantity=int(quantity))
                return render(request, "rath/partials/success.html", {"item": item})
            else:
                cart = cart.add(product=item, quantity=int(quantity))
                return render(request, "rath/partials/success.html", {"item": item})
    else:
        return JsonResponse({"data": "Error"}, status=403)


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return render(request, "rath/partials/success.html")
