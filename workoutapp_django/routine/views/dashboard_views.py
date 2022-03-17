from cgitb import reset
from users.models import CustomUser

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import RoutineCategory, UserRoutine, ExerciseCategory, UserWorkout, Exercise, UserExercise
from ..serializers import RoutineCategorySerializer, UserRoutineSerializer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

# FOR TESTING
import time
from django.db import connection, reset_queries

# Create your views here.

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def GetUserWorkouts(request, username, workout_id):
#     user = CustomUser.objects.get(username=username)
#     workout = Workout.objects.get(user_id=user.id)
#     workout_serialized = WorkoutSerializer(workout)
#     return Response(workout_serialized.data)

class GetAllUserRoutines(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_routines = UserRoutine.objects.filter(user_id=request.user.id)
        user_routines_serialized = UserRoutineSerializer(user_routines, many=True)
        return Response(user_routines_serialized.data)

class CreateUserRoutine(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        new_routine_name = request.data["routineName"]
        new_routine_categories = request.data["routineCategories"]
        new_routine_isPrivate = request.data["isPrivate"]

        new_routine = UserRoutine.objects.create(user=request.user, name=new_routine_name, is_private=new_routine_isPrivate)
        new_routine.save()
        
        for category in new_routine_categories:
            category = RoutineCategory.objects.filter(name=category)
            new_routine.categories.add(category[0])

        return Response("Routine successfully created")

class CreateUserWorkout(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_routine_id = request.data["routineId"]
        workout_name = request.data["workoutName"]
        user_exercises = request.data["userExercises"]

        user_routine = UserRoutine.objects.get(pk=user_routine_id)
        new_workout = UserWorkout.objects.create(routine=user_routine, name=workout_name)
        new_workout.save()

        for user_exercise in user_exercises:
            exercise = Exercise.objects.get(pk=user_exercise['exerciseId'])
            new_workout.user_exercises.create(exercise=exercise, order=user_exercise['order'], description=user_exercise['description'])

        return Response("Workout successfully created")

#TODO: Check if a new exercise has been added
#TODO: Checks if field has been changed to reduce DB calls
class UpdateUserWorkout(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        reset_queries()

        id = request.data["userWorkoutId"]
        updated_name = request.data["name"]
        updated_user_exercises = request.data["userExercises"]

        # Update User Workout Fields
        user_workout = UserWorkout.objects.get(pk=id)
        if user_workout.name != updated_name:
            user_workout.name = updated_name
            user_workout.save()

        #Update User Exercise Fields
        for updated_user_exercise in updated_user_exercises:
            user_exercise = UserExercise.objects.get(pk=updated_user_exercise["userExerciseId"])
            write_fields(user_exercise, 
                description=updated_user_exercise["description"],
                order=updated_user_exercise["order"],
                exercise=Exercise.objects.get(pk=updated_user_exercise["exerciseId"]))


        # user_exercises = UserExercise.objects.filter(workout_id=user_workout.id)
        # for user_exercise in user_exercises:
        #     for updated_user_exercise in updated_user_exercises:
        #         if user_exercise.id == updated_user_exercise['userExerciseId']:
        #             should_save = False
        #             if user_exercise.exercise.id != updated_user_exercise['exerciseId']:
        #                 should_save = True
        #                 user_exercise.exercise = Exercise.objects.get(pk=updated_user_exercise['exerciseId'])
        #             if user_exercise.order != updated_user_exercise['order']:
        #                 should_save = True
        #                 user_exercise.order = updated_user_exercise['order']
        #             if user_exercise.description != updated_user_exercise['description']:
        #                 should_save = True
        #                 user_exercise.description = updated_user_exercise['description']

        #             if should_save:
        #                 user_exercise.save()
        #             break

        for query in connection.queries:
            print(str(query) + "\n")

        return Response("User Workout Updated")

def write_fields(obj, **kwargs):
        should_save = False
        
        for k, v in kwargs.items():
            if getattr(obj, k) != v:
                setattr(obj, k, v)
                should_save = True

        if should_save:
            obj.save(update_fields=kwargs.keys())



           









