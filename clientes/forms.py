from django import forms
from .models import Cliente

class ClienteCreationForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('documento', 'nombre', 'tipo_documento') # Incluye los campos que necesites para la creación
        # Puedes personalizar los widgets, etiquetas, etc. aquí

class ClienteAuthenticationForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = ('documento', 'password')
    
