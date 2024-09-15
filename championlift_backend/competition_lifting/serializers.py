# competition_powerlift/serializers.py

from rest_framework import serializers
from .models import Competitor

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = '__all__'  # O especifica los campos que deseas incluir