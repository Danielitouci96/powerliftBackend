# competition_powerlift/serializers.py

from rest_framework import serializers
from .models import Competitor, Lift

class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = ['id', 'name', 'weight']

class CompetitorSerializer(serializers.ModelSerializer):
    lift_history = LiftSerializer(many=True, read_only=True)
    latest_lift = LiftSerializer(read_only=True)

    class Meta:
        model = Competitor
        fields = ['id', 'name', 'age', 'weight', 'height', 'weight_class', 'profile_image', 'lift_history', 'latest_lift']