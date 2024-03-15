from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class VariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # Create multiple objects
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Create a single object
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


