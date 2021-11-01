from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Menu, Category, Cart

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class ReviewCart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')


class MenuPage(View):
    def get(self, request, *args, **kwargs):
        # menu = Menu.objects.all()

        pizza_custom = Menu.objects.filter(category__name__contains='Create Your Own Pizza')
        pizza_8 = Menu.objects.filter(category__name__contains='8" Specialty Pizza')
        pizza_12 = Menu.objects.filter(category__name__contains='12" Thin Crust Specialty Pizza')

        context = {
            'pizza_custom': pizza_custom,
            'pizza_8': pizza_8,
            'pizza_12': pizza_12
        }

        return render(request, 'menu.html', context)

    def post(self, request, *args, **kwargs):
        cart_items = []
        items = request.POST.getlist('items[]')    # IDs from items selected from the user

        for item in items:
            temp_item = Menu.objects.get(pk=int(item))    # Menu item from database that contains the ID
            item_data = {   # Store relevant info
                'id': temp_item.pk,
                'name': temp_item.name,
                'price': temp_item.price
            }
            cart_items.append(item_data)

        price = 0
        item_id = []

        for item in cart_items:
            price += item['price']
            item_id.append(item['id'])

        cart = Cart.objects.create(price=price)
        # cart.price = price
        cart.items.add(*item_id)

        context = {
            'items': cart_items,
            'price': price
        }

        return render(request, 'cart.html', context)


class Checkout(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'checkout.html')
