from django.conf import settings
from django.contrib import admin
from django.urls import path,include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('DATA/',include('DATA.urls')),
]


