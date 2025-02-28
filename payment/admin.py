from django.contrib import admin
from payment.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "currency")

    search_fields = ("name", "description")
    list_filter = ("currency",)
    ordering = ("name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("get_items", "items_for_delete")

    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
