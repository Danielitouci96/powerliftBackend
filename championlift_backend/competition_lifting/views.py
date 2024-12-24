# competition_powerlift/views.py

from rest_framework import generics
from .models import Competitor, Lift, Modality
from .serializers import CompetitorSerializer, LiftSerializer, ModalitySerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from .models import Competitor
from .serializers import CompetitorSerializer

class CompetitorList(generics.ListCreateAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer

class CompetitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competitor.objects.prefetch_related('lift_history')
    serializer_class = CompetitorSerializer

class ModalityList(generics.ListAPIView):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer

class LiftCreate(generics.CreateAPIView):
    serializer_class = LiftSerializer

    def perform_create(self, serializer):
        competitor_id = self.kwargs['competitor_id']  # Obtén el ID del competidor de la URL
        try:
            competitor = Competitor.objects.get(id=competitor_id)
            serializer.save(competitor=competitor)  # Asocia el levantamiento con el competidor
        except Competitor.DoesNotExist:
            raise serializer.ValidationError("Competitor not found")

# Asegúrate de que esta vista esté incluida en tus URLs

class LiftDelete(generics.DestroyAPIView):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={ 'message': 'Deleted successfully'})
        
class LiftDetail(generics.RetrieveUpdateAPIView):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer

    def update(self, request, *args, **kwargs):
        lift = self.get_object()
        serializer = self.get_serializer(lift, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)