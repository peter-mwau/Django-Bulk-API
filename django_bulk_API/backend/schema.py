# schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Product, ProductVariant

class ProductVariant(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = ('product_variant_id', 'product_sku', 'variant_name', 'price', 'variant_details', 'foreignKey') 

class ProductVariantInput(graphene.InputObjectType):
    product_variant_id = graphene.String()
    product_sku = graphene.String()
    variant_name = graphene.String()
    price = graphene.Float()
    variant_details = graphene.String()
    foreignKey = graphene.String()


class BulkInsertData(graphene.Mutation):
    class Arguments:
        data = graphene.List(ProductVariantInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, data):
        for item in data:
            ProductVariant.objects.create(**item)
        return BulkInsertData(success=True)

class Mutation(graphene.ObjectType):
    bulk_insert_data = BulkInsertData.Field()

class Query(graphene.ObjectType):
    product_variants = graphene.List(ProductVariant)

    def resolve_product_variants(self, info):
        return ProductVariant.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
