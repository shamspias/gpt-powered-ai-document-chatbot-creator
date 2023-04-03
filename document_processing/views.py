from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from .tasks import process_document


class DocumentListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        document_type = self.request.data.get('document_type')
        file = self.request.FILES.get('file')
        url = self.request.data.get('url')

        document_id = process_document.delay(self.request.user.id, document_type, file, url)
        serializer.save(user=self.request.user, document_type=document_type, pinecone_index_id=document_id)


class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
