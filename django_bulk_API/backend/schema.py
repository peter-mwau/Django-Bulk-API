# schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Product, ProductVariant


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'image')
class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = ('product_variant_id', 'product_sku', 'variant_name', 'price', 'variant_details', 'foreignKey') 


class ProductInput(graphene.InputObjectType):
    product_id = graphene.ID()
    product_name = graphene.String()
    image = graphene.String()


class ProductVariantInput(graphene.InputObjectType):
    product_variant_id = graphene.String()
    product_sku = graphene.String()
    variant_name = graphene.String()
    price = graphene.Float()
    variant_details = graphene.String()
    # foreignKey = graphene.Int()
    product = graphene.InputField(ProductInput)


class BulkInsertData(graphene.Mutation):
    class Arguments:
        data = graphene.List(ProductVariantInput)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, data):
        for item in data:
            product_data = item.pop('product')  # Extract product data
            product = Product.objects.create(**product_data)  # Create the related product
            item['foreignKey'] = product.pk  # Assuming 'foreignKey' is the ForeignKey field in ProductVariant
            ProductVariant.objects.create(**item)  # Create the ProductVariant instance
        return BulkInsertData(success=True)

class Mutation(graphene.ObjectType):
    bulk_insert_data = BulkInsertData.Field()

class Query(graphene.ObjectType):
    product_variants = graphene.List(ProductVariantType)

    def resolve_product_variants(self, info):
        return ProductVariant.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
