from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from .models import Document
from .serializers import DocumentSerializer
from .tasks import process_file
from .utils import get_source_type


class DocumentUploadView(generics.CreateAPIView):
    """
    View for uploading a document (PDF, CSV, or URL).
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        source_type = get_source_type(self.request.data['file'])
        instance = serializer.save(user=self.request.user, source_type=source_type)
        task = process_file.apply_async(args=[instance.id, instance.file.path, source_type])
        response = task.get()
        print(response)
