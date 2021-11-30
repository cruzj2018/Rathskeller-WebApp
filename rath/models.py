from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200, help_text="Enter section name")
    slug = models.SlugField(
        max_length=200, unique=True, help_text="Slug title (unique identifier)"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    items = models.ManyToManyField("Item")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Food Section"


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, unique=True, help_text="Slug title (unique identifier)"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "Categories"


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=255, help_text="Food name")
    slug = models.SlugField(max_length=255, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ("-created",)