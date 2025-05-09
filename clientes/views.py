from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

def get_object(pk):
    try:
        return Cliente.objects.get(pk=pk)
    
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

#lista de clientes
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show(request, pk):
    cliente = get_object(pk)
    serializer = ClienteSerializer(cliente)
    return Response(serializer.data)
    
@api_view(['PUT', 'PATCH'])
def update(request, pk):
    cliente = get_object(pk)
    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
    elif request.method == 'PATCH':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def destroy(request, pk):
    cliente = get_object(pk)
    cliente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    

    


