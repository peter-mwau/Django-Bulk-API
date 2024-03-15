from rest_framework import serializers
from .models import Product, ProductVariant

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'image']

class ProductVariantSerializer(serializers.ModelSerializer):
    foreignKey = ProductSerializer()
    class Meta:
        model = ProductVariant
        fields = ['product_variant_id', 'product_sku', 'variant_name', 'price', 'variant_details', 'foreignKey']