from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        return Response('OK')

@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product,context={'request': request})
    return Response(serializer.data)


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
    