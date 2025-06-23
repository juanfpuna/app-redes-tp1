
from rest_framework import serializers

from facturas.models import Factura, DetalleFactura

from clientes.serializers import ClienteSerializer
from facturas.detalleserializer import DetalleFacturaSerializer
from clientes.models import Cliente



class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True, read_only=True)
    cliente_info = ClienteSerializer(read_only=True, source='cliente')
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    
    class Meta:
        model = Factura
        fields = '__all__'
        
        
class FacturaBasicaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True, read_only=True)
    class Meta:
        model = Factura
        fields = ['id', 'cod_factura', 'fecha_emision', 'total_factura', 'estado', 'detalles']
        


        