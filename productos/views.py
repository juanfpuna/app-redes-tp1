from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from productos.models import Producto
from productos.serializers import ProductoSerializer

@api_view(['GET'])
def index(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def store(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()        
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, pk):
    producto = Producto.objects.get(pk=pk)
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.update()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, pk):
    
    try:
    
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
