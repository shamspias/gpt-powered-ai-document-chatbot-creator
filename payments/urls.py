from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('subscription/', views.SubscriptionRetrieveUpdateView.as_view(), name='subscription_retrieve_update'),
]
