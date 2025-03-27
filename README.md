# Aplicaciones en redes - Trabajo Practico
Proyecto de la clase de Programacion de Aplicaciones de Redes. Trabajo Practico

**Prerrequisitos:**

* **Python:** Asegúrate de tener Python 3.7+ instalado. Puedes verificarlo ejecutando `python --version` o `python3 --version` en tu terminal.
* **pip:** Asegúrate de tener `pip` (el instalador de paquetes de Python) instalado. Generalmente viene con Python. Verifica con `pip --version` o `pip3 --version`.
* **Entorno Virtual (Recomendado):** Es altamente recomendable usar un entorno virtual para aislar las dependencias de tu proyecto.

**Pasos:**

**1. Crear un Entorno Virtual (Opcional pero Recomendado):**

* Navega al directorio raíz de tu proyecto (`app-redes-tp1`) en tu terminal.
* Crea un entorno virtual:

    ```bash
    python3 -m venv venv  # O python -m venv venv
    ```

    Esto crea un directorio llamado `venv` (puedes nombrarlo diferente si quieres) que contendrá tu entorno.
* Activa el entorno virtual:
    * Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    * Windows:

        ```bash
        venv\Scripts\activate
        ```

    Deberías ver `(venv)` al principio de tu prompt de terminal, indicando que el entorno está activo.

**2. Instalar Django:**

* Con tu entorno virtual activado, instala Django:

    ```bash
    pip install django
    sudo apt install python3-django #Usuarios linux
    ```

**3. Navegar al Directorio del Proyecto:**

* Asegúrate de que estás en el directorio raíz de tu proyecto (`app-redes-tp1`).

**3-1 Instalar libreria restframework**

* Para el funcionamiento del servicio de REST API es necesario tener instalado la libreria correspondiente. Esta libreria se encarga 
de la serializacion de los modelos y la creacion de las rutas para las peticiones. Para instalar: 


```
pip install djangorestframework
sudo apt install python3-djangorestframework #Usuarios linux

```

**4. Aplicar Migraciones:**

* Django usa migraciones para gestionar los cambios en el esquema de la base de datos. Ejecuta los siguientes comandos para crear y aplicar las migraciones iniciales:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    Esto creará las tablas de base de datos necesarias basadas en tus archivos `models.py`.

**5. Crear un Superusuario (Usuario Administrador):**

* Para acceder a la interfaz de administración de Django, necesitas un superusuario:

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las indicaciones para crear un nombre de usuario, correo electrónico y contraseña.

**6. Ejecutar el Servidor de Desarrollo:**

* Inicia el servidor de desarrollo de Django:

    ```bash
    python manage.py runserver
    ```

    Deberías ver una salida en tu terminal indicando que el servidor se está ejecutando, generalmente en `http://127.0.0.1:8000/`.

**7. Acceder a la Aplicación:**

* Abre tu navegador web y ve a `http://127.0.0.1:8000/`. Deberías ver la página de bienvenida predeterminada de Django.
* **Acceder al Administrador:** Ve a `http://127.0.0.1:8000/admin/` e inicia sesión con las credenciales de superusuario que creaste.
* **Accediendo a las otras apps:**
    * http://127.0.0.1:8000/facturas/
    * http://127.0.0.1:8000/clientes/
    * http://127.0.0.1:8000/proveedores/
    * http://127.0.0.1:8000/productos/

**8. Detener el Servidor**

* Presiona `Ctrl+C` en la terminal donde el servidor se está ejecutando.


**Resumen de Comandos Clave:**

* `python manage.py makemigrations`: Crea archivos de migración basados en los cambios en tus modelos.
* `python manage.py migrate`: Aplica las migraciones a la base de datos.
* `python manage.py createsuperuser`: Crea un usuario administrador.
* `python manage.py runserver`: Inicia el servidor de desarrollo.