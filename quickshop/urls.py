from django.contrib import admin
from django.urls import path, include # Импортируйте include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')), # Все URL из catalog теперь корневые
]

# Это нужно для работы с медиа-файлами (изображениями) в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
