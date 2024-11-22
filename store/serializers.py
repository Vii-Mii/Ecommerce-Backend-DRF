from rest_framework import serializers
from decimal import Decimal
from .models import Collection, Product

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length =255)
    
    class Meta:
        model = Collection
        fields = ['id','title']
    

class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2,source='unit_price')
    # price_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection_detail',
    #     lookup_field='id'
    # )
    
    class Meta:
        model = Product
        fields = ['id','title','description','inventory','unit_price','price_with_tax','collection']
        read_only_fields = ['id']
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    def calculate_tax(self,product):
        return product.unit_price * Decimal(1.1)
    