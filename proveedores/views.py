from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from proveedores.models import Proveedor
from proveedores.serializers import ProveedorSerializer

def get_object( pk):
    try: 
        return Proveedor.objects.get(pk=pk)
    except Proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def show(request, pk):
    proveedor = get_object(pk)
    serializer = ProveedorSerializer(proveedor)
    return Response(serializer.data)
       
@api_view(['PUT', 'PATCH'])
def update(request, pk):
    proveedor = get_object(pk)

    if request.method == 'PUT':
    
        serializer = ProveedorSerializer(proveedor, data=request.data)
    elif request.methid == 'PATCH':
        serializer = ProveedorSerializer(proveedor, data=request.data, partial=True)
        
    if(serializer.is_valid()):
        serializer.update()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, pk):
    
    proveedor = get_object(pk)
    proveedor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
