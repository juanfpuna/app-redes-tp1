
from rest_framework import serializers

from facturas.models import Factura, DetalleFactura


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
        read_only_fields = ('id', 'cliente', 'fecha_emision')
        
class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = '__all__'
        read_only_fields = ('id', 'factura', 'producto')
    
        

        