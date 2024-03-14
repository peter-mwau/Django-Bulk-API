from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_name
    
class ProductVariant(models.Model):
    product_variant_id = models.AutoField(primary_key=True)
    product_sku = models.CharField(max_length=100)
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    variant_details = models.CharField(max_length=100)
    foreignKey = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.variant_name
