import copy
from decimal import Decimal
import json
from django.conf import settings
from rath.models import Item
from django.core.serializers.json import DjangoJSONEncoder


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Item.objects.filter(id__in=product_ids)

        # cart = self.cart.copy()
        cart = copy.deepcopy(self.cart)
        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def add(self, product, quantity=1, override_quantity=False, extra=None):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if extra:
            self.cart[product_id]["extra"] = json.dumps(
                list(extra), cls=DjangoJSONEncoder
            )
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

        print(self.cart)

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )
