
from rest_framework.decorators import api_view


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from clientes.models import Cliente

from clientes.forms import ClienteCreationForm, ClienteAuthenticationForm

@api_view(['GET','POST'])
def autenticarse(request):
    if request.method == 'POST':
        try:
            
            errors = {}
            
            documento = request.POST.get('documento')
            password = request.POST.get('password')
            user = authenticate(documento=documento, password=password)

            print(documento, password, user)

            
            login(request, user)
            return redirect('productos')
            
           
        
               
        except Exception as e:
                   
                    errors['general'] = f'Ocurrió un error al iniciar sesion: {e}'
                    return render(request, 'autenticacion/login.html', {'errors': errors, 'form_data': request.POST})
    else:
        if request.user.is_authenticated:
            return redirect('productos')
        
    return render(request, 'autenticacion/login.html')

@api_view(['POST'])
def cerrar_sesion(request):
    logout(request)
    return redirect('autenticarse')


def registrarse(request):
    errors = {}
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        documento = request.POST.get('documento')
        email = request.POST.get('email')
        tipo_documento = request.POST.get('tipo_documento')
        direccion = request.POST.get('direccion')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        # --- VALIDACIÓN DE DATOS ---
        if not nombre:
            errors['nombre'] = 'El nombre es requerido.'
        if not documento:
            errors['documento'] = 'El documento es requerido.'
        # Puedes agregar más validaciones para el formato del documento si es necesario
        if password != re_password:
            errors['re_password'] = 'Las contraseñas no coinciden.'
        if len(password) < 8:  # Ejemplo de validación de longitud de contraseña
            errors['password'] = 'La contraseña debe tener al menos 8 caracteres.'
        try:
            Cliente.objects.get(documento=documento)
            errors['documento'] = 'Ya existe un cliente con este documento.'
        except Cliente.DoesNotExist:
            pass  # No existe, podemos continuar

        if errors:
            print(errors)
            return render(request, 'autenticacion/registrarse.html', {'errors': errors, 'form_data': request.POST}, status=500)
        else:
            # --- CREACIÓN DEL USUARIO ---
            try:
                cliente = Cliente.objects.create(
                    nombre=nombre,
                    documento=documento,
                    # email=email,
                    tipo_documento=tipo_documento,
                    direccion=direccion,  
                    password=make_password(password)  # Hashea la contraseña
                )


                login(request, cliente)
                return redirect('home')
            except Exception as e:

                print(e)
                errors['general'] = f'Ocurrió un error al crear la cuenta: {e}'
                return render(request, 'autenticacion/registrarse.html', {'errors': errors, 'form_data': request.POST}, 500)

    return render(request, 'autenticacion/registrarse.html')


