from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    filters = models.ManyToManyField('Filter', related_name='item')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)
    filters = models.ManyToManyField('Filter', related_name='topping')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):   # To do: validate the answer. It may be exploitable.
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('Menu', related_name='cart', blank=True)
    name = models.CharField(max_length=100, blank=True)
    student_id = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Order: {self.date.strftime("%b %d %I: %M %p")}'
