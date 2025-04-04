from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from facturas.models import Factura
from facturas.serializers import FacturaSerializer

@api_view(['GET', 'POST'])

def get_object(pk):
    try:
        return Factura.objects.get(pk=pk)
    
    except Factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

def index(request):
    if request.method == 'GET':
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update(request, pk):
    factura = get_object(pk)
    
    if request.method == 'PUT':    
        serializer = FacturaSerializer(factura, data=request.data)
    elif request.method == 'PATCH':
        serializer = FacturaSerializer(factura, data=request.data, partial=True)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete(request, pk):
    factura = get_object(pk)
    factura.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
