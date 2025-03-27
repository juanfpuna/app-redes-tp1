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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

