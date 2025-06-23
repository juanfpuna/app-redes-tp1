
from rest_framework import serializers

from facturas.models import DetalleFactura
from productos.models import Producto

from productos.serializers import ProductoSerializer


class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(), # Necesario para validar que el ID existe
        source='producto',               
        write_only=True                  
    )
    
    
    class Meta:
        model = DetalleFactura
        fields = ['id', 'factura','producto', 'cantidad', 'total', 'producto_id']

    
        