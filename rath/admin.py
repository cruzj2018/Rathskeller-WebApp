from django.contrib import admin
from .models import Category, Item, Section, ItemAttribute, DietType

class DietTypeAdmin(admin.ModelAdmin):
    list_display = ("diet_name", "diet_description","get_display_title")


admin.site.register(DietType, DietTypeAdmin)

class ItemAttributeInline(admin.TabularInline):
    model = ItemAttribute
    extra = 0
    readonly_fields = ("selected", )

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "slug",
    )
    list_select_related = ("category",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ItemAttributeInline, )



admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created", "updated")
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Category, CategoryAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created",)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Section, SectionAdmin)
