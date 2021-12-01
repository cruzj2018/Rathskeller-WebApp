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


class DietType(models.Model):
    diet_name = models.CharField(max_length=255)
    diet_description = models.TextField()

    def __str__(self):
        return self.diet_name


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=255, help_text="Food name")
    slug = models.SlugField(max_length=255, unique=True)
    diet = models.ForeignKey(DietType, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField()
    item_image = models.ImageField(upload_to="items/image", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_price(self):
        return "{:.2f}".format(self.price)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ("-created",)


class ItemAttribute(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item_attributes"
    )
    name = models.CharField(max_length=100)
    extra_cost = models.IntegerField()
    selected = models.BooleanField(default=True)

    def __str__(self):
        return self.name
