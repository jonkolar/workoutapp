from rest_framework import serializers
from .models import RoutineCategory, UserRoutine, WorkoutCategory, UserWorkout, Exercise, UserExercise

class RoutineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineCategory
        fields = "__all__"

class UserRoutineSerializer(serializers.ModelSerializer):
    categories = RoutineCategorySerializer(many=True)
    class Meta:
        model = UserRoutine
        fields = "__all__"

# class SetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Set
#         fields = "__all__"
        

# class WorkoutExerciseSerializer(serializers.ModelSerializer):
#     exercise = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='name'
#     )
#     sets = SetSerializer(many=True)
#     class Meta:
#         model = WorkoutExercise
#         fields =  (
#             "id",
#             "order",
#             "workout",
#             "exercise",
#             "sets"
#         )

# class WorkoutSerializer(serializers.ModelSerializer):
#     exercises = WorkoutExerciseSerializer(many=True)
#     class Meta:
#         model = Workout
#         fields =  (
#             "id",
#             "user_id",
#             "name",
#             "exercises"
#         )

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"

# class ExerciseSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     class Meta:
#         model = Exercise
#         fields = (
#             "id",
#             "name",
#             "category"
#         )