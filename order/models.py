import uuid
from django.db import models
from django.contrib.sessions.models import Session
# from phonenumber_field.modelfields import PhoneNumberField
from rath.models import Item

def order_id_generator():
    return uuid.uuid4().hex[:11].upper()

class OrderItem(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    quantity = models.IntegerField()

class Order(models.Model):
    order_number = models.CharField(max_length=11, unique=True, default=order_id_generator)
    created_date = models.DateTimeField(auto_now_add=True)
    order_items = models.ManyToManyField(OrderItem)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    data = models.JSONField()

    def __str__(self):
        return self.order_number


