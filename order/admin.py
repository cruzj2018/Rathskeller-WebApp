from django.contrib import admin
from .models import OrderItem, Order

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    # inlines = (OrderItemInline, )

    search_fields = ("order_number", "created_date")


admin.site.register(Order, OrderAdmin)