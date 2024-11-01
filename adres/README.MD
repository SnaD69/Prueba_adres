# Prueba Técnica para Full Stack
Este proyecto consiste en una aplicación web desarrollada en Django que permite a los usuarios cargar un archivo CSV. La aplicación valida la estructura del archivo de acuerdo a criterios específicos definidos en los requisitos. El objetivo es garantizar que los datos se ingresen en un formato adecuado y que cumplan con las restricciones establecidas.

### Requisitos de la prueba 
El archivo CSV que se cargará debe cumplir con las siguientes condiciones:

Número de Columnas: El archivo debe contener exactamente 5 columnas. Si contiene más o menos columnas, la aplicación alertará al usuario.
Columna 1: Esta columna debe contener solo números enteros con una longitud de entre 3 y 10 caracteres.
Columna 2: Debe contener correos electrónicos válidos.
Columna 3: Solo se permiten los valores "CC" o "TI".
Columna 4: Los valores deben estar entre 500,000 y 1,500,000.
Columna 5: Esta columna puede contener cualquier valor.

### Funcionalidades

Carga de Archivos: Los usuarios pueden cargar archivos CSV a través de un formulario en la interfaz web.
Validación de Datos: Al cargar el archivo, la aplicación valida cada fila y columna según los criterios especificados.
Mensajes de Resultado: La aplicación mostrará mensajes que indican si la validación fue exitosa o si se encontraron errores, incluyendo la fila y columna correspondiente a cada error.
Interfaz Amigable: La interfaz está diseñada para ser intuitiva, facilitando la carga y la visualización de resultados.


## Prerequisitos
Antes de comenzar, asegúrate de tener instalado:

- Python (versión 3.x)
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado para crear entornos virtuales)

## Instalación
Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

### Clonar el Repositorio
Primero, clona el repositorio de Git a tu máquina local utilizando el siguiente comando:

### bash
git clone https://github.com/SnaD69/Prueba_adres.git

### Crear y Activar un Entorno Virtual (Opcional)
Es recomendable utilizar un entorno virtual para mantener las dependencias del proyecto separadas y organizadas. Para crear y activar un entorno virtual, ejecuta:

virtualenv venv

### En Windows
venv\Scripts\activate

### En Unix o MacOS
source venv/bin/activate

### Instalar Dependencias
Instala todas las dependencias requeridas para el proyecto ejecutando:

pip install -r requirements.txt

### Configuración de la Base de Datos
Configura tu base de datos según las necesidades de tu proyecto.
en este proyecto se utilizo como base de datos SQL Server si va a utilizar otro tipo de gestor de base de datos realizar la modificacion en settings.py

### Migraciones Iniciales
Antes de ejecutar el servidor, realiza las migraciones iniciales con:

python manage.py makemigrations
python manage.py migrate

### Crear un Superusuario (Opcional)
Para acceder al panel de administración de Django, crea un superusuario:

python manage.py createsuperuser

### Ejecutar el Servidor de Desarrollo
Finalmente, inicia el servidor de desarrollo con:

python manage.py runserver

y dirijase a http://localhost/validar_csv/

