from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from proveedores.models import Proveedor
from proveedores.serializers import ProveedorSerializer


@api_view(['GET'])
def index(request):
    proveedores = Proveedor.objects.all()
    serializer = ProveedorSerializer(proveedores, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def store(request):
    serializer = ProveedorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

