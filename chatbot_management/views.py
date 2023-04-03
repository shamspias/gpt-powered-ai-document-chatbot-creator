from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Chatbot
from .serializers import ChatbotSerializer


class ChatbotListView(generics.ListCreateAPIView):
    """
    View for listing and creating chatbots.
    """
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChatbotDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting chatbots.
    """
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
