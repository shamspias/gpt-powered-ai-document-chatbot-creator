from django.urls import path
from . import views

urlpatterns = [
    path('chatbots/', views.ChatbotListView.as_view(), name='chatbot_list'),
    path('chatbots/<int:pk>/', views.ChatbotDetailView.as_view(), name='chatbot_detail'),
]
