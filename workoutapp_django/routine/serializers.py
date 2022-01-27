from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = "__all__"
        

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)
    class Meta:
        model = WorkoutExercise
        fields =  (
            "id",
            "order",
            "workout",
            "exercise",
            "sets"
        )

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True)
    class Meta:
        model = Workout
        fields =  (
            "id",
            "name",
            "exercises"
        )