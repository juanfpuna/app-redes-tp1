from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from facturas.models import Factura
from facturas.serializers import FacturaSerializer

@api_view(['GET'])
def index(request):
    facturas = Factura.objects.all()
    serializer = FacturaSerializer(facturas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def store(request):
    serializer = FacturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, pk):
    factura = Factura.objects.get(pk=pk)
    serializer = FacturaSerializer(factura, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return

@api_view(['DELETE'])
def delete(request, pk):
    try: 
        factura = Factura.objects.get(pk=pk)
        factura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
