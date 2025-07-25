# competition_powerlift/views.py

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Competitor, Lift, Modality, UserStaff
from .serializers import CompetitorSerializer, LiftSerializer, ModalitySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .models import Competitor
from .serializers import CompetitorSerializer
from .utils import ipf_gl_points, get_best_lifts

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
    
class UserList(viewsets.ModelViewSet):
    queryset = UserStaff.objects.all()
    serializer_class = UserSerializer

class CalculateIPFPoints(APIView):
    """
    Endpoint para calcular y actualizar los puntos IPF GL de un competidor
    """
    def post(self, request, pk):
        try:
            competitor = Competitor.objects.get(pk=pk)
            lift_history = list(competitor.lift_history.all())
            best = get_best_lifts(lift_history)

            total_points = 0.0
            # Suma de puntos calculados lift por lift
            total_points += ipf_gl_points(best.get('squat', 0), competitor.weight, competitor.gender)
            total_points += ipf_gl_points(best.get('bench', 0), competitor.weight, competitor.gender)
            total_points += ipf_gl_points(best.get('deadlift', 0), competitor.weight, competitor.gender)

            competitor.ipf_points = round(total_points, 3)
            competitor.save()

            return Response({
                "ipf_points": competitor.ipf_points,
                "best_lifts": best,
                "competitor": CompetitorSerializer(competitor).data,
            })
        except Competitor.DoesNotExist:
            return Response({"error": "Competitor not found"}, status=status.HTTP_404_NOT_FOUND)