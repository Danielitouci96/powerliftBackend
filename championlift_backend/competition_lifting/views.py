# competition_powerlift/views.py

from rest_framework import generics
from .models import Competitor
from .serializers import CompetitorSerializer

from rest_framework import generics
from .models import Competitor
from .serializers import CompetitorSerializer

class CompetitorList(generics.ListCreateAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer

class CompetitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer
