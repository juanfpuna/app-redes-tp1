import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from facturas.models import Factura, DetalleFactura
from facturas.serializers import FacturaSerializer, DetalleFacturaSerializer


from clientes.models import Cliente

from productos.models import Producto
from productos.serializers import ProductoSerializer

def get_object(pk):
    try:
        return Factura.objects.get(pk=pk)
    
    except Factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'Factura no encontrada'})
    

@api_view(['GET', 'POST'])
def index(request):
    
    facturas = Factura.objects.all()
    serializer = FacturaSerializer(facturas, many=True)
    return Response(serializer.data)
   
@api_view(['GET'])
def show(request, pk):
    try:
        factura = Factura.objects.prefetch_related('detalles').get(pk=pk)
        
        serializer = FacturaSerializer(factura)
        return Response(serializer.data)
    except Factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'La factura solicitada no existe'})
    
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= {'error': str(e)})
    

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
    

@api_view(['POST'])
def iniciar_venta(request):
    try : 
        cliente = Cliente.objects.get(pk=request.data.get('cliente'))
        cod_factura = datetime.datetime.now().strftime('%m%d%H%M')
        serializer = FacturaSerializer(data={
            'cliente': cliente.id,
            'nombre_empleado': request.data.get('nombre_empleado'),
            'cod_factura': cod_factura,
            'fecha_emision': datetime.date.today(),
            
            })
        
        if serializer.is_valid():
        
            factura = serializer.save()
            
            
            return Response(FacturaSerializer(factura).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    except cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= {'error': str(e)})
        

@api_view(['POST'])
def agregar_producto(request, pk):
    try:
        factura = Factura.objects.get(pk=pk)
        
        if factura.estado != 'abierta':
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {'error': 'La venta ya fue cerrada'})
        
        producto = Producto.objects.get(pk=request.data.get('producto'))
        
        
        if producto.stock < request.data.get('cantidad'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {'error': 'No hay suficiente stock. Stock actual es de ' + str(producto.stock) + ' unidades'})
        
        detalle_factura = DetalleFacturaSerializer(
            data={'factura': factura.id, 
                  'producto': producto.id, 
                  'cantidad': request.data.get('cantidad'), 
                  'total': producto.precio_venta * request.data.get('cantidad')})
        
        if detalle_factura.is_valid():
            detalle_factura.save()
        
            return Response(detalle_factura.data, status=status.HTTP_201_CREATED)
        
        return Response(detalle_factura.errors, status=status.HTTP_400_BAD_REQUEST)
    except factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'La factura solicitada no existe'})
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'Producto no encontrado'})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= {'error': str(e)}) 
        
    
@api_view(['PATCH'])
def cerrar_venta(request, pk):
    
    try:
        
    
        factura = Factura.objects.get(pk=pk)
        
        if factura.estado != 'abierta':
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {'error': 'La venta ya fue ' + factura.estado})
        
        for detalle in factura.detalles.all():
            producto = detalle.producto
            producto.stock = producto.stock - detalle.cantidad
            producto.save()
            factura.total_factura = factura.total_factura + detalle.total
        
        factura.estado = 'cerrada'
        factura.save()
        
        return Response(status=status.HTTP_200_OK, data={"total": factura.total_factura, "cant_productos": factura.detalles.count()})
    
    except DetalleFactura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'Detalle de factura no encontrado'})
    
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= {'error': str(e)})
            
@api_view(['POST'])
def anular_venta(request, pk):
    
    try:
        factura = Factura.objects.get(pk=pk)
        
        if factura.estado != 'abierta':
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {'error': 'No se puede anular una factura con estado ' + factura.estado})
        
        
        factura.estado = 'anulada'
        factura.save()
        return Response(status=status.HTTP_200_OK, data= {'mensaje': 'Factura anulada correctamente'})
    
    except factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'La factura solicitada no existe'})
    
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data= {'error': str(e)})

@api_view(['DELETE', 'PATCH'])
def actualizar_detalles(request, pk_factura, pk_detalle):
    
    
    try:
        
        factura = Factura.objects.get(pk=pk_factura)
        if factura.estado != 'abierta':
            return Response(status=status.HTTP_400_BAD_REQUEST, data= {'error': 'No se puede modificar un detalle de factura con estado ' + factura.estado})
    
        if request.method == 'DELETE':
        
            detalle_factura = DetalleFactura.objects.get(pk=pk_detalle)
            detalle_factura.delete()
            factura = Factura.objects.get(pk=pk_factura)
            factura.total = factura.total - detalle_factura.total
            factura.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PATCH':
            
            detalle_factura = DetalleFactura.objects.get(pk=pk_detalle)
            restar_detalle = detalle_factura.total
            detalle_factura.cantidad = request.data.get('cantidad')
            detalle_factura.total = detalle_factura.producto.precio * request.data.get('cantidad')
            detalle_factura.save()
            factura = Factura.objects.get(pk=pk_factura)
            factura.total = factura.total - restar_detalle + detalle_factura.total
            factura.save()
            return Response(status=status.HTTP_200_OK)
            
    except DetalleFactura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= {'error': 'Detalle de factura no encontrado'})



    
    
    
    
        
            
    
