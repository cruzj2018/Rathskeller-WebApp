from django.shortcuts import render, get_object_or_404
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from rath.models import Item
from .models import OrderItem
from .cart import Cart

# Create your views here.


def order_list(request):
    ordered_items = OrderItem.objects.all()
    return render(request, "order/order_items.html", {"ordered_items": ordered_items})


def add_item(request):
    if request.method == "POST":
        # request.session['cart'] = ""
        cart = Cart(request)
        if request.htmx:
            item_id = request.POST.get("item-id")
            quantity = request.POST.get("total")
            selected = request.POST.getlist('selected')

            cart = Cart(request)
            item = get_object_or_404(Item , id=item_id)
            
            cart.add(product=item, quantity=int(quantity))

            # cart.clear()

            for c in cart:
                print(c)
                        
            # data = {"item_id": item_id}
        # return JsonResponse({"data": data}, status=200)
            return render(request, "rath/partials/success.html", {"item": item})
    else:
        return JsonResponse({"data": "Error"}, status=403)
