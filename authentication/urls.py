from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView,
    PasswordChangeView, UserDetailsView, PasswordResetConfirmView, PasswordResetView
)
from rest_auth.views import (
    PasswordResetConfirmView, PasswordResetView, PasswordChangeView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from .views import (
    GoogleLogin, CustomLogoutView, UserCreateAPIView, UserUpdateAPIView,
    CustomSocialAccountListView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', CustomLogoutView.as_view(), name='rest_logout'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('register/', UserCreateAPIView.as_view(), name='rest_register'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('user/update/', UserUpdateAPIView.as_view(), name='rest_user_update'),
    path('account-email-verification-sent/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    path('account-confirm-email/<str:key>/', VerifyEmailView.as_view(),
         name='account_confirm_email'),
    path('accounts/', include('allauth.urls')),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    path('social/accounts/', CustomSocialAccountListView.as_view(), name='social_account_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
