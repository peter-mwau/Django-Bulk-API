from django.contrib import admin
from .models import Product, ProductVariant
# list display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'image')


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product_variant_id', 'product_sku', 'variant_name', 'price', 'variant_details', 'foreignKey')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
