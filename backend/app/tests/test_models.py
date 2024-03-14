from django.test import TestCase
from ..models import File

class FileModelTest(TestCase):
    @classmethod
    # Test setup/ Configuração do teste
    def setUpTestData(cls):
        File.objects.create(name='Test File', picture='example.jpg')

    # Check if the Django File model has/
    # verificam se o modelo Django File possui:

    # A name field with a maximum length of 30 characters/
    # Um campo name com comprimento máximo de 30 caracteres.
    def test_name_field(self):
        file_obj = File.objects.get(id=1)
        max_length = file_obj._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    # A picture field configured to upload to the 'media' directory/
    # Um campo picture configurado para fazer upload para o diretório 'media'.
    def test_picture_field(self):
        file_obj = File.objects.get(id=1)
        upload_to = file_obj._meta.get_field('picture').upload_to
        self.assertEquals(upload_to, 'media')

    # The ability to create a File object with the name field set to 'Test File'/
    # A capacidade de criar um objeto File com o campo name definido como 'Test File'.
    def test_object_creation(self):
        file_obj = File.objects.get(id=1)
        self.assertEqual(file_obj.name, 'Test File')