from django.contrib import admin
from .models import Cards, Order

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'product_total_price', 'created')
    list_display_links = ('user', 'product', 'quantity', 'product_total_price', 'created')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'payment_status', 'created', 'updated')
    list_display_links = ('user', 'total_price', 'payment_status', 'created', 'updated')