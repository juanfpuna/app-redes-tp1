from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from productos.models import Producto
from productos.serializers import ProductoSerializer
from django.views import View
from django.shortcuts import render



@api_view(['GET'])
def show(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        return render(request, 'productos/producto.html', {'producto': serializer.data})
        # return Response(serializer.data)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error' : 'Producto no encontrado'})

@api_view(['GET','POST'])
def index(request):
    try: 
        productos = Producto.objects.all()
        if request.method == 'GET':
            serializer = ProductoSerializer(productos, many=True)
            usuario = request.user
            
            return render(request, 'productos/index.html', {'productos': serializer.data, 'usuario' : usuario})
            
            # return Response(serializer.data)
        if request.method == 'POST':
            serializer = ProductoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()        
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data= {'error' :str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['PUT', 'PATCH'])
def update(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = ProductoSerializer(producto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = ProductoSerializer(producto, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error' : 'Producto no encontrado'})
        

@api_view(['DELETE'])
def delete(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error' : 'Producto no encontrado'})
    
    
    
