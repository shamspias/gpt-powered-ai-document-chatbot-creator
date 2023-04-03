from django.urls import path
from . import views

app_name = 'question_answering'

urlpatterns = [
    path('conversations/', views.ConversationListView.as_view(), name='conversation_list'),
    path('conversations/<int:pk>/', views.ConversationDetailView.as_view(), name='conversation_detail'),
]
