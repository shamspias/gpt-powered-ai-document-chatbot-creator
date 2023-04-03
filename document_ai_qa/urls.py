from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="chatbot builder API",
        default_version='v1',
        description="API for chatbot builder",
        terms_of_service="https://github.com/shamspias",
        contact=openapi.Contact(email="shamspias0@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('question_answering/', include('question_answering.urls')),
                  path('chatbot_management/', include('chatbot_management.urls')),
                  path('auth/', include('authentication.urls'), name='auth'),
                  path('document_processing/', include('document_processing.urls')),
                  path('payments/', include('payments.urls')),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
