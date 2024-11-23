from rest_framework import serializers
from decimal import Decimal
from .models import Collection, Product, Review

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length =255)
    
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Collection
        fields = ['id','title','product_count']
        read_only_fields = ['id','product_count']
        
    def get_product_count(self, obj):
        # The 'obj' is the Collection instance, and we want to get the count of related products
        return obj.product_set.count()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','inventory','unit_price','price_with_tax','collection']
        read_only_fields = ['id']
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    def calculate_tax(self,product):
        return product.unit_price * Decimal(1.1)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date','product']
    