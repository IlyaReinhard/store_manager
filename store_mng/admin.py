from django.contrib import admin
from .models import Product, Delivery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_of_product','count_kg_product','price_of_kg','making_date', 'expiration_date', 'produced_before')

@admin.register(Delivery)
class DeliveruAdmin(admin.ModelAdmin):
    list_display = ['delivery_date']