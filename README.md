Examen Final: Desarrollo de Backend - Catálogo Bibliográfico
Este proyecto constituye la entrega del Examen Final para la materia de Desarrollo de Aplicaciones Web. Consiste en un sistema Backend de alta disponibilidad que gestiona un catálogo de Autores y Libros, diseñado para ser consumido de forma asíncrona por un cliente Frontend en React.

Datos del estudiante
Nombre: Carlos Alejandro Tene Mora

Carrera: Ingeniería de Software

Materia: Desarrollo de Aplicaciones Web

Tecnologías y Arquitectura
Framework: Django 6.0.2 con Django Rest Framework (DRF).

Seguridad: Protocolo OAuth2 mediante django-oauth-toolkit.

Base de Datos: SQLite3.

Manejo de Imágenes: Procesamiento de archivos mediante serializadores en formato Base64.

Características Implementadas
Seguridad por Niveles: * Lectura (GET): Pública para todos los usuarios.

Escritura (POST, PUT, DELETE): Protegida mediante IsAuthenticated y TokenHasScope.

Scopes de OAuth2: Uso de scopes específicos (write) para restringir acciones administrativas.

CORS: Configurado para permitir la integración transparente con React.

Instalación y Configuración
Ejecuta los siguientes comandos en tu terminal CMD:

1. Preparar el Ambiente
DOS
python -m venv venv
.\venv\Scripts\activate
2. Instalar Dependencias
DOS
pip install django djangorestframework django-oauth-toolkit django-cors-headers pillow
pip freeze > requirements.txt
3. Base de Datos y Servidor
DOS
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Endpoints de la API
Autores: http://127.0.0.1:8000/api/autores/

Libros: http://127.0.0.1:8000/api/libros/

Autenticación: http://127.0.0.1:8000/o/token/

Pasos finales en tu VS Code:
Guarda el archivo README.md.

Súbelo a GitHub con estos comandos en tu terminal:

DOS
git add README.md
git commit -m "docs: actualizar README con formato CMD para el examen final"
git push origin main