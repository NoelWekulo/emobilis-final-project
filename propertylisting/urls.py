from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('propertyapp.urls')),
]# Include URLs from blog app

# Append static URL configuration for media files
if settings.DEBUG:  # Only use this in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
