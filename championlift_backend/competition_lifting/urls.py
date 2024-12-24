# competition_powerlift/urls.py

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import CompetitorDetail, CompetitorList, LiftCreate, LiftDetail, ModalityList, LiftDelete

urlpatterns = [
    path('competitors/', CompetitorList.as_view(), name='competitor-list'),  # Para listar y crear competidores
    path('competitors/<int:pk>/', CompetitorDetail.as_view(), name='competitor-detail'),  # Para obtener, actualizar y eliminar un competidor
    path('modalities/', ModalityList.as_view(), name='modality-list'),  # Nueva URL para modalidades
    path('competitors/<int:competitor_id>/lifts/', LiftCreate.as_view(), name='lift-create'),
    path('lifts/<int:pk>/', LiftDetail.as_view(), name='lift-detail'),  # URL para actualizar levantamientos por ID
    path('lifts/<int:pk>/delete/', LiftDelete.as_view(), name='lift-delete'),  # URL para eliminar levantamientos por ID
    
]

if settings.DEBUG:  # Solo para desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)