from rest_framework import serializers
from .models import *

# FileSerializer:
# Class responsible for serializing objects of the File model.
# Defines which fields of the model will be included in the serialization.
# Classe responsável por serializar objetos do modelo File.
# Define quais campos do modelo serão incluídos na serialização.

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'picture']