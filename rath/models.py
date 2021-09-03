from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vegan = models.BooleanField(default=False)
