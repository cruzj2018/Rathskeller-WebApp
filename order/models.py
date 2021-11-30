import uuid
from django.db import models
from rath.models import Item

def order_id_generator():
    return uuid.uuid4().hex[:11].upper()

class OrderItem(models.Model):
    items = models.ManyToManyField(Item)
    quantity = models.IntegerField()
    order = models.ForeignKey("Order", related_name="orders", on_delete=models.CASCADE)

class Order(models.Model):
    order_number = models.CharField(max_length=11, unique=True, default=order_id_generator)
    created_date = models.DateTimeField(auto_now_add=True)

