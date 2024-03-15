from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, VariantViewSet


router = routers.DefaultRouter()
router.register(r'products', VariantViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
