from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

    
