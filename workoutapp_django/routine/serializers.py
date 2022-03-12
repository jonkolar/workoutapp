from rest_framework import serializers
from .models import RoutineCategory, UserRoutine, WorkoutCategory, UserWorkout, Exercise, UserExercise

# ADD WORKOUT CATEGORY

class WorkoutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutCategory
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    categories = WorkoutCategorySerializer(many=True)

    class Meta:
        model = Exercise
        fields = "__all__"

class UserExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()

    class Meta: 
        model = UserExercise
        fields = "__all__"

class UserWorkoutSerializer(serializers.ModelSerializer):
    user_exercises = UserExerciseSerializer(many=True)

    class Meta:
        model = UserWorkout
        fields = ("id", "name", "categories", "date_added", "user_exercises")

class RoutineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineCategory
        fields = "__all__"

class UserRoutineSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    categories = RoutineCategorySerializer(many=True)
    user_workouts = UserWorkoutSerializer(many=True)

    def get_user(self, obj):
        return {'username': obj.user.username, 'user_id': obj.user.id}

    class Meta:
        model = UserRoutine
        fields = ("id", "name", "user", "is_private", "categories", "user_workouts")

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