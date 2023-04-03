from django.urls import path
from . import views

app_name = 'document_processing'

urlpatterns = [
    path('documents/', views.DocumentListCreateView.as_view(), name='document_list_create'),
    path('documents/<int:pk>/', views.DocumentRetrieveUpdateDestroyView.as_view(),
         name='document_retrieve_update_destroy'),
]
