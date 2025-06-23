from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum



def get_object(pk):
    try:
        return Cliente.objects.get(pk=pk)
    
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    

#lista de clientes
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)

        clientes_con_totales = Cliente.objects.annotate(
            total_gastado=Sum('facturas__total_factura'))
        
        clientes_con_gastos_reales = clientes_con_totales.exclude(total_gastado__isnull=True)
        
        cliente_mayor_comprador = clientes_con_gastos_reales.order_by('-total_gastado').first()

        return render(request, 'cliente/index.html', {'clientes': serializer.data, 'cliente_mayor_comprador': cliente_mayor_comprador})
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():

            nombre = request.data.get('nombre')
            documento = request.data.get('documento')
            tipo_documento = request.data.get('tipo_documento')
            direccion = request.data.get('direccion')
            password = request.data.get('password')


            print(nombre, documento, tipo_documento, direccion, password, request.data.get('is_superuser', False))

            cliente = Cliente.objects.create(
                    nombre=nombre,
                    documento=documento,
                    is_superuser= request.data.get('is_superuser', False),
                    tipo_documento=tipo_documento,
                    direccion=direccion,  
                    password=make_password(password)  # Hashea la contraseña
                )
            

            print(cliente)
            
            serializer = ClienteSerializer(cliente)


            print(serializer.data)


            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show(request, pk):
    cliente = get_object(pk)
    serializer = ClienteSerializer(cliente)
    return Response(serializer.data)
    
@api_view(['PUT', 'PATCH'])
def update(request, pk):
    cliente = get_object(pk)
    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
    elif request.method == 'PATCH':
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def destroy(request, pk):
    cliente = get_object(pk)
    cliente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def autenticarse(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            documento = form.cleaned_data.get('documento')
            password = form.cleaned_data.get('password')
            user = authenticate(documento=documento, password=password)
            if user is not None:
                login(request, user)
                return redirect('productos')  # Redirige a la página de inicio
            else:
                form.add_error(None, 'Documento o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})

@api_view(['GET'])
def perfil(request):
    if request.user.is_authenticated:
        
        cliente = Cliente.objects.get(documento=request.user.documento)
        factura = cliente.facturas.filter(estado = 'abierta').first()
        serializer = ClienteSerializer(cliente)
        
        return render(request, 'cliente/perfil.html', {'usuario': serializer.data})
    
    else:
        return redirect('autenticacion/login.html')



