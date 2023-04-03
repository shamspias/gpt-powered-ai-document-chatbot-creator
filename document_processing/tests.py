from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Document


class DocumentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.document = Document.objects.create(
            user=self.user,
            document_type='PDF',
            content='Sample text extracted from the PDF file',
            pinecone_index_id='sample_pinecone_index_id'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_create_document(self):
        """
        Ensure we can create a new document object.
        """
        url = reverse('document_processing:document_list_create')
        data = {'document_type': 'URL', 'url': 'https://example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 2)

    def test_list_documents(self):
        """
        Ensure we can list documents.
        """
        url = reverse('document_processing:document_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_document(self):
        """
        Ensure we can retrieve a document.
        """
        url = reverse('document_processing:document_retrieve_update_destroy', args=[self.document.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['document_type'], 'PDF')

    def test_update_document(self):
        """
        Ensure we can update a document.
        """
        url = reverse('document_processing:document_retrieve_update_destroy', args=[self.document.id])
        data = {'document_type': 'URL', 'url': 'https://example.com'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Document.objects.get(id=self.document.id).document_type, 'URL')

    def test_delete_document(self):
        """
        Ensure we can delete a document.
        """
        url = reverse('document_processing:document_retrieve_update_destroy', args=[self.document.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Document.objects.count(), 0)
