from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import File
from PIL import Image
import tempfile

class VueViewTest(TestCase):
    @classmethod
    # Test setup/ Configuração do teste.
    def setUpTestData(cls):
        # Create a test user/ Criar um usuário de teste.
        cls.user = User.objects.create_user(username='testuser', password='12345')

    def setUp(self):
        # Create a JWT token for the test user/ Criar um token JWT para o usuário de teste.
        self.token = AccessToken.for_user(self.user)
        self.client = APIClient()
        # Pass the JWT token in the 'Authorization' header to authenticate requests/
        # Passar o token JWT no cabeçalho 'Authorization' para autenticar as solicitações.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

    # Test: Get all data/ recupera todos os dados.
    def test_get_method(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # Test: Insert new data/ Insere um novo dado.
    def test_post_method(self):
        #  Create a test image/ Criar uma imagem de teste.
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(tmp_file)

        # Create the file to send in the request/
        # Montar o arquivo para enviar na requisição.
        image.seek(0)
        image_data = SimpleUploadedFile(tmp_file.name, image.tobytes(), content_type='image/png')

        # Data to send in the request/
        # Dados para enviar na requisição.
        data = {'name': 'New File', 'picture': image_data}

        # Send POST request/
        # Enviar a requisição POST.
        response = self.client.post('', data, format='multipart')

        # Check if the response returns code 201 (Created)/
        # Verificar se a resposta retorna o código 201 (Created).
        self.assertEqual(response.status_code, 201)

    # Test: Delete data/ deleta dado.
    def test_delete_method(self):
        # Create a test object and delete the same object/
        # Cria um objeto teste e deleta o mesmo objeto.
        file = File.objects.create(name='Test File', picture='example.jpg')
        response = self.client.delete(f'/delete/{file.id}')
        self.assertEqual(response.status_code, 204)

    # Test: Get all data/ recupera todos os dados.
    def test_get_method(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


    # Error tests / testes de erro.
    def test_post_method_without_name(self):
        # Send a POST request without providing the file name/
        # Enviar uma requisição POST sem fornecer o nome do arquivo
        data = {'picture': SimpleUploadedFile("test_image.png", b"file_content", content_type='image/png')}
        response = self.client.post('', data, format='multipart')
        self.assertEqual(response.status_code, 400)

    # Test: Error when trying to insert without an image/
    # Erro ao tentar inserir sem uma imagem.
    def test_post_method_without_picture(self):
        data = {'name': 'New File'}
        response = self.client.post('', data)
        self.assertEqual(response.status_code, 400)

    def test_post_method_invalid_picture(self):
        # Send a POST request with an invalid image/
        # Enviar uma requisição POST com uma imagem inválida.
        data = {'name': 'New File', 'picture': 'invalidImage'}
        response = self.client.post('', data, format='multipart')
        self.assertEqual(response.status_code, 400)

    def test_post_method_with_large_name(self):
        # Send a POST request with a very long filename/
        # Enviar uma requisição POST com um nome de arquivo muito longo.
        data = {
            'name': 'This is a very long name that exceeds the maximum allowed length',
            'picture': SimpleUploadedFile("test_image.png", b"file_content", content_type='image/png')
        }
        response = self.client.post('', data, format='multipart')
        self.assertEqual(response.status_code, 400)

    def test_delete_method_nonexistent_file(self):
        # Try to delete a file that does not exist/
        # Tentar excluir um arquivo que não existe.
        response = self.client.delete('/delete/999')
        self.assertEqual(response.status_code, 404)