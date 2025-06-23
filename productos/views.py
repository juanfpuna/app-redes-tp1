from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from productos.models import Producto
from productos.serializers import ProductoSerializer
from django.views import View
from django.shortcuts import render, redirect

from proveedores.models import Proveedor
from django.db.models import Sum






@api_view(['GET'])
def show(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        
       
        
        return render(request, 'productos/producto.html', {'producto': serializer.data})
        # return Response(serializer.data)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error' : 'Producto no encontrado'})
    
@api_view(['GET'])
def edit(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        proveedores = Proveedor.objects.all()
        return render(request, 'productos/editar.html', {'producto': serializer.data, 'proveedores': proveedores})
        
    except producto.DoesNotExist:
        return redirect('productos')
    

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
                return redirect('productos')
            # Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data= {'error' :str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['POST'])
def update(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
        
        serializer = ProductoSerializer(producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
        return redirect('productos')

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
    
    
    
@api_view(['GET'])
def create(request):
    proveedores = Proveedor.objects.all()    
    return render(request, 'productos/crear.html', {'proveedores': proveedores})

@api_view(['GET'])
def stock(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    productos_con_cantidades = Producto.objects.annotate(total_unidades_vendidas=Sum('detallefactura__cantidad'))
    productos_vendidos = productos_con_cantidades.exclude(total_unidades_vendidas__isnull=True)
    producto_mas_vendido = productos_vendidos.order_by('-total_unidades_vendidas').first()
    return render(request, 'productos/stock.html', {'productos': serializer.data, 'producto_mas_vendido': producto_mas_vendido})