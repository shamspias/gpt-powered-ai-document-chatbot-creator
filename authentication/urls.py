from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('google-login/', views.GoogleLoginView.as_view(), name='google_login'),
    path('request-reset-email/', views.RequestPasswordResetEmail.as_view(), name='request_reset_email'),
    path('reset-password/', views.SetNewPasswordAPIView.as_view(), name='reset_password'),
]
