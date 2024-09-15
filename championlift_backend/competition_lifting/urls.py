# competition_powerlift/urls.py

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import CompetitorDetail, CompetitorList

urlpatterns = [
    path('competitors/', CompetitorList.as_view(), name='competitor-list'),  # Para listar y crear competidores
    path('competitors/<int:pk>/', CompetitorDetail.as_view(), name='competitor-detail'),  # Para obtener, actualizar y eliminar un competidor
]

if settings.DEBUG:  # Solo para desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)