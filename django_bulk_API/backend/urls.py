from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, VariantViewSet
from graphene_django.views import GraphQLView
from .schema import schema


router = routers.DefaultRouter()
router.register(r'products', VariantViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
