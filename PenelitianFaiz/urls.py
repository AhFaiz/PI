from django.conf import settings
from django.contrib import admin
from django.urls import path,include

from .views import index
import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('DATA/',include('DATA.urls')),
]

urlpatterns += (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += (settings.STATIC_URL, document_root = settings.STATIC_ROOT)


