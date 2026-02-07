from rest_framework import serializers  
from .models import Autor, Libro
from django.core.files.base import ContentFile
import base64
import uuid

class LibroSerializer(serializers.ModelSerializer):
    portada = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Libro
        fields = '__all__'

    def validate_portada(self, value):
        if value and ';base64,' in value:
            format, imgstr = value.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
            return data
        return value

class AutorSerializer(serializers.ModelSerializer):
    imagen = serializers.CharField(required=False, allow_null=True)
    libros = LibroSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'fecha_nacimiento', 'nacionalidad', 'bibliografia', 'imagen', 'libros']

    def validate_imagen(self, value):
        if value and ';base64,' in value:
            format, imgstr = value.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
            return data
        return value