from rest_framework import serializers
from clientes.models import Cliente



class ClienteSerializer(serializers.ModelSerializer):
    facturas = serializers.SerializerMethodField()
    
    def get_facturas(self, obj):
        from facturas.serializers import FacturaBasicaSerializer
        
        return FacturaBasicaSerializer(obj.facturas.all(), many=True).data
    
    class Meta:
        model = Cliente
        fields = ('documento', 'nombre','direccion', 'estado', 'date_joined', 'last_login', 'facturas')
        
class ClienteBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'documento', 'nombre'] 
        
        
        
        