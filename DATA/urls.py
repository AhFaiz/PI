from django.urls import path

from .views import IndexData

urlpatterns = [
    path('', IndexData),
]