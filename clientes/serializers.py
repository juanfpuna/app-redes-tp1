from rest_framework import serializers
from clientes.models import Cliente
from django.db.models import Sum



class ClienteSerializer(serializers.ModelSerializer):
    facturas = serializers.SerializerMethodField()
    total_compras = serializers.SerializerMethodField()
    
    def get_facturas(self, obj):
        from facturas.serializers import FacturaBasicaSerializer
        
        return FacturaBasicaSerializer(obj.facturas.all(), many=True).data
    
    def get_total_compras(self, obj):
        """
        Calcula el total de todas las facturas (compras) de un cliente.
        """
        total_agregado = obj.facturas.aggregate(total_compras=Sum('total_factura'))
        
        return total_agregado['total_compras'] if total_agregado['total_compras'] is not None else 0.00
    
    class Meta:
        model = Cliente
        fields = ('documento', 'nombre','direccion', 'estado', 'date_joined', 'last_login', 'facturas', 'total_compras', 'is_superuser', 'id')
        
class ClienteBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'documento', 'nombre'] 
        
        
        
        