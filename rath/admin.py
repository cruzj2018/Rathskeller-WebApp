from django.contrib import admin
from .models import Category, Item, Section

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "slug",
    )
    list_select_related = ("category",)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created", "updated")
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CategoryAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created",)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Section, SectionAdmin)
