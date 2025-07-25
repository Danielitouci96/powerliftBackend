# competition_powerlift/serializers.py

from rest_framework import serializers
from .models import Competitor, Lift, Modality, UserStaff
from django.contrib.auth.hashers import make_password

class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = ['id', 'name', 'weight', 'competitor', 'valid']  # Asegúrate de incluir 'competitor'

class CompetitorSerializer(serializers.ModelSerializer):
    lift_history = LiftSerializer(many=True, read_only=True)
    latest_lift = LiftSerializer(read_only=True)

    class Meta:
        model = Competitor
        fields = [
            'id', 'name', 'age', 'weight', 'height',
            'weight_class', 'profile_image', 'lift_history',
            'latest_lift', 'ipf_points', 'gender'
        ]


class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserStaff
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        # Encriptar la contraseña antes de guardar
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)