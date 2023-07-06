# Control de Nómina de Empleados

Esta es una aplicación de ejemplo para el control de nómina de empleados utilizando Python, Django y Django Rest Framework.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>```
1. Ve al directorio del proyecto:

cd control_nomina

2. Crea y activa un entorno virtual (opcional, pero se recomienda):

python -m venv venv
source venv/bin/activate

3. Instala las dependencias:

pip install Django
pip install djangorestframework

# Configuracion de la Base de Datos

Esta aplicación utiliza la base de datos SQLite por defecto. No se requiere ninguna configuración adicional.

#Migraciones de la Base de Datos

1. Aplica las migraciones para crear las tablas de la base de datos:

python manage.py migrate

2. Crea un superusuario para acceder al panel de administración:

python manage.py createsuperuser

Sigue las instrucciones para proporcionar un nombre de usuario, 
dirección de correo electrónico (opcional) y contraseña. 
Por ejemplo, puedes utilizar los siguientes valores:

Username: Daniel
Email address: (leave blank)
Password: facil123
Password (again): facil123

# Ejecucion del Servidor de Desarrollo

1. Inicia el servidor de desarrollo de Django:

python manage.py runserver

2. Abre tu navegador web y accede a la siguiente URL:

http://127.0.0.1:8000/

Esto te llevará a la interfaz de la API, donde puedes realizar las operaciones CRUD en los empleados.

3.  Para acceder al panel de administración, ve a la siguiente URL:

http://127.0.0.1:8000/admin/

Ingresa las credenciales de superusuario que creaste anteriormente (por ejemplo, username: Daniel, password: facil123).

# Informe de Nomina

Puedes generar un informe de nómina que muestra el nombre del empleado,
 salario y el total de la nómina. Para ello, utiliza el siguiente endpoint:
 
GET /nomina/informe/

Este endpoint proporcionará un informe en formato JSON con el total de la nómina y los detalles de los empleados.

# Autenticación y Autorización

Esta aplicación no implementa autenticación y autorización en la protección de los endpoints de la API. Se recomienda implementar estas funcionalidades en un entorno de producción para garantizar la seguridad de los datos.

# Licencia

Este proyecto se distribuye bajo la Licencia MIT. Puedes consultar el archivo LICENSE para obtener más información.

Recuerda reemplazar `<URL_DEL_REPOSITORIO>` en el paso 1 con la URL de tu repositorio si deseas proporcionar un enlace directo para clonar el repositorio.

Espero que esto te sea útil para crear el archivo `README.md` y documentar adecuadamente tu aplicación de control de nómina de empleados.