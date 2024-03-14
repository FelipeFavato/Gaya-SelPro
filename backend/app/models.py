from django.db import models

# class File:
# Model to represent a file.
# Has fields id, name, and picture.
# id: Unique identifier of the file.
# name: Name of the file, with a maximum of 30 characters.
# picture: Image file to be uploaded to the 'media' directory.

# Modelo para representar um arquivo.
# Possui os campos id, name, e picture.
# id: Identificador único do arquivo.
# name: Nome do arquivo, com no máximo 30 caracteres.
# picture: Arquivo de imagem a ser carregado para o diretório 'media'.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    picture = models.FileField(upload_to='media')