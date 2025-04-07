
from rest_framework import serializers

from facturas.models import Factura, DetalleFactura

from productos.serializers import ProductoSerializer


class DetalleFacturaSerializer(serializers.ModelSerializer):
    # producto = ProductoSerializer()
    
    
    class Meta:
        model = DetalleFactura
        fields = '__all__'

    
        