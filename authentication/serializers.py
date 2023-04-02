from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for the User model.
    """

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'profile_picture']
        read_only_fields = ['id', 'email']


class CustomRegisterSerializer(RegisterSerializer):
    """
    A custom serializer that extends the default RegisterSerializer to include
    additional fields.
    """
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        setup_user_email(request, user, [])
        adapter.save_user(request, user, self)
        return user


class CustomSocialLoginSerializer(serializers.Serializer):
    """
    A custom serializer that extends the default SocialLoginSerializer to include
    additional fields.
    """
    access_token = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['email'] = attrs.get('email') or self.user.email or ''
        attrs['first_name'] = attrs.get('first_name')
        attrs['last_name'] = attrs.get('last_name')
        return attrs
