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
    best_total = serializers.SerializerMethodField()

    class Meta:
        model = Competitor
        fields = [
            'id', 'name', 'age', 'weight', 'height',
            'weight_class', 'profile_image', 'lift_history',
            'latest_lift', 'ipf_points', 'gender', 'best_total'
        ]
    
    def get_best_total(self, obj):
        """
        Obtiene los mejores levantamientos válidos para squat, bench y deadlift.
        Nombres normalizados a minúsculas.
        """
        lift_history = obj.lift_history.filter(valid='valid')
        squat_names = {'cuclilla', 'squad', 'squat', 'cuclilla(squad)'}
        bench_names = {'press de banca', 'bench', 'bench press'}
        deadlift_names = {'peso muerto', 'deadlift'}

        best = {'squat': 0.0, 'bench': 0.0, 'deadlift': 0.0}

        for lift in lift_history:
            if lift.valid != 'valid':
                continue
            lname = lift.name.strip().lower()
            if lname in squat_names:
                best['squat'] = max(best['squat'], lift.weight)
            elif lname in bench_names:
                best['bench'] = max(best['bench'], lift.weight)
            elif lname in deadlift_names:
                best['deadlift'] = max(best['deadlift'], lift.weight)
        
        sum_best = best['squat'] + best['bench'] + best['deadlift']

        return sum_best



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