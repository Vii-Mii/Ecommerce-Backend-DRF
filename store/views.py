from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer,CollectionSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response("Product cannot be deleted as associated with orderitems",status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def collection_list(request):
    queryset = Collection.objects.all()
    serializer = CollectionSerializer(queryset,many = True,context={'request': request})
    return Response(serializer.data)

@api_view()
def collection_detail(request,id):
    collection = get_object_or_404(Collection,pk=id)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
    