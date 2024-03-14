from rest_framework import serializers
from .models import Product, ProductVariant

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    foreign_key = ProductSerializer()
    class Meta:
        model = ProductVariant
        fields = '__all__'