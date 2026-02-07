# Examen Final. Desarrollo de Backend: API REST, Catálogos y OAuth2

Este proyecto constituye la entrega del **Examen Final** para la materia de Desarrollo de Aplicaciones Web. Consiste en un sistema Backend de alta disponibilidad que gestiona un catálogo de Autores y Libros, diseñado para ser consumido de forma asíncrona por un cliente Frontend. Utilizando como framework de desarrollo Django y Django Rest Framework.

Por otra parte se aplica el uso de Modelos en Django, uso de bases de datos relacionales y seguridad avanzada mediante el protocolo OAuth2.

Además el manejo de Django desde el desarrollo de API REST, uso de serializadores complejos, manejo de imágenes en Base64 y configuración de permisos mediante Scopes.

## Datos del estudiante
- **Nombre:** Carlos Alejandro Tene Mora
- **Carrera:** Ingeniería de Software

## Objetivos 
- El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) para la creación de modelos relacionales.
- El estudiante reforzará sus conocimientos de desarrollo Backend mediante la implementación de una arquitectura desacoplada.
- El estudiante desarrollará un sistema de seguridad robusto con OAuth2 para la protección de endpoints sensibles.

## Tareas a realizar
1. Generación de Modelos de Autor y Libro.
2. Generación de migraciones y administración de base de datos.
3. Implementación de API REST con Django Rest Framework.
4. Configuración de OAuth2 Toolkit para autenticación y manejo de Scopes.

## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- SQLite3
- Configurar el repositorio local
    ~~~
    git config --local user.name "Carlos Alejandro Tene Mora"
    ~~~
    ~~~
    git config --local user.email "[Tu Email de Github]"
    ~~~

### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
python -m venv venv
~~~
Activación del ambiente virtual para CMD
~~~
.\venv\Scripts\activate
~~~
Instalación de dependencias de este proyecto
~~~
pip install django djangorestframework django-oauth-toolkit django-cors-headers pillow
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles

### Iniciar servidor
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion>
~~~

### Crear Súper Usuario
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Windows
~~~
python manage.py migrate
~~~

### Almacenar dependencias y librerías instaladas
#### Windows
~~~
pip freeze > requirements.txt
~~~

# Configuración de Base de Datos para el Examen

### SQLite (Utilizada en este proyecto)
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

### Endpoints de la API
- **Autores:** `http://127.0.0.1:8000/api/autores/`
- **Libros:** `http://127.0.0.1:8000/api/libros/`
- **Autenticación (OAuth2):** `http://127.0.0.1:8000/o/token/`
