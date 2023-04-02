from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_auth.views import LogoutView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics

from .serializers import UserSerializer, CustomSocialLoginSerializer


class GoogleLogin(SocialLoginView):
    """
    A view that handles Google social authentication.
    """
    adapter_class = GoogleOAuth2Adapter


class CustomLogoutView(LogoutView):
    """
    A view that logs out the user.
    """
    permission_classes = [AllowAny]


class UserCreateAPIView(generics.CreateAPIView):
    """
    A view that creates a new user.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    A view that updates an existing user's information.
    """
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CustomSocialAccountListView(generics.ListAPIView):
    """
    A view that lists the authenticated user's social accounts.
    """
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        queryset = user.socialaccount_set.all()
        return queryset
