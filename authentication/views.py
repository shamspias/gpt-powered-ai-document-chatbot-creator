from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import (
    UserSerializer, UserProfileSerializer, RegisterSerializer, TokenObtainPairSerializer,
    ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
)
from .utils import Util
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


# Registration view
class RegisterView(generics.CreateAPIView):
    """
    Register a new user.
    """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


# User profile view
class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    User profile view
    """
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'

    def get_object(self):
        return self.request.user.userprofile


# Google login view
class GoogleLoginView(generics.GenericAPIView):
    """
    Google login view.
    """
    serializer_class = TokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        # Implement the logic to exchange the code for access_token, id_token, and user profile
        # Then, obtain or create the user and generate JWT tokens
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


# Request password reset email view
class RequestPasswordResetEmail(generics.GenericAPIView):
    """
    Request password reset email view.
    """
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            # Implement sending email with reset password link
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Set new password view
class SetNewPasswordAPIView(generics.GenericAPIView):
    """
    Set new password view.
    """
    serializer_class = SetNewPasswordSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            token = serializer.validated_data['token']
            uidb64 = serializer.validated_data['uidb64']

            # Decode the user ID and get the user instance
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
            except (User.DoesNotExist, ValueError, OverflowError):
                return Response({"error": "Invalid token or user ID"}, status=status.HTTP_400_BAD_REQUEST)

            # Verify the token and update the user's password
            if not default_token_generator.check_token(user, token):
                return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(password)
            user.save()

            return Response({"message": "Password has been reset"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
