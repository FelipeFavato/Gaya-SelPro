from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
# import boto3
# import botocore

# VueView:
# View class for Vue.js integration.
# Implements GET, POST, and DELETE methods for file manipulation.
# Classe de visualização para integração com Vue.js.
# Implementa métodos GET, POST e DELETE para manipulação de arquivos.
class VueView(APIView):

    # GET:
    # Returns a list of all files.
    # Each file is represented as a dictionary with fields id, name, and picture.
    # picture is the absolute URL of the image, if it exists.

    # Retorna uma lista de todos os arquivos.
    # Cada arquivo é representado como um dicionário com os campos id, name, e picture.
    # picture é a URL absoluta da imagem, se existir.
    def get(self, request):
        output = [
            { "id": output.id, "name": output.name, "picture": request.build_absolute_uri(output.picture.url) if output.picture else None }
            for output in File.objects.all()
        ]
        return Response(output)


    # POST:
    # Creates a new file based on the provided data.
    # Validates the data using FileSerializer.
    # If the data is valid, saves the file and returns the created file data with status 201 (Created).
    # If the data is invalid, returns the validation errors with status 400 (Bad Request).

    # Cria um novo arquivo com base nos dados fornecidos.
    # Valida os dados usando FileSerializer.
    # Se os dados forem válidos, salva o arquivo e retorna os dados do arquivo criado com status 201 (Created).
    # Se os dados forem inválidos, retorna os erros de validação com status 400 (Bad Request).
    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            error_response = {}
            for field, error in errors.items():
                error_response[field] = error[0]  # Take the first error message for each field
            return Response({"errors": error_response}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE:
    # Deletes a file based on the provided ID.
    # Returns status 204 (No Content) if deletion is successful.
    # Returns status 404 (Not Found) if the file is not found.
    # Returns status 500 (Internal Server Error) if an unexpected error occurs.
        
    # Exclui um arquivo com base no ID fornecido.
    # Retorna status 204 (No Content) se a exclusão for bem-sucedida.
    # Retorna status 404 (Not Found) se o arquivo não for encontrado.
    # Retorna status 500 (Internal Server Error) se ocorrer algum erro inesperado.
    def delete(self, request, pk):
        try:
            file = File.objects.get(id=pk)
            file.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except File.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Developing download service:
    # def download(self, pk):
    #     BUCKET_NAME = 'gayasimulationsbucket'
    #     file = File.objects.get(id=pk)
    #     KEY = str(file.picture)
    #     print(KEY)

    #     s3 = boto3.resource('s3')

    #     try:
    #         # Unable to locate credentials
    #         s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
    #     except botocore.exceptions.ClientError as e:
    #         if e.response['Error']['Code'] == "404":
    #             print("The object does not exist.")
    #         else:
    #             raise