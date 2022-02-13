from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise, Set

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = "__all__"
        

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
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
            "user_id",
            "name",
            "exercises"
        )