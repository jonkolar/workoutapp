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
            print(user_exercise)
            exercise = Exercise.objects.get(pk=user_exercise['exerciseId'])
            new_workout.user_exercises.create(exercise=exercise, order=user_exercise['order'], description=user_exercise['description'])

        return Response("Workout successfully created")

# class GetAllCategories(APIView):
#     def get(self, request):
#         all_categories = Category.objects.all()
#         all_categories_serialized = CategorySerializer(all_categories, many=True)
#         return Response(all_categories_serialized.data)

# class GetExercises(APIView):
#     def get(self, request, category):
#         exercises = Exercise.objects.filter(category=category)
#         exercises_serialized = ExerciseSerializer(exercises, many=True)
#         return Response(exercises_serialized.data)

# class CreateWorkout(APIView):
#     def post(self, request):
#         createdWorkout = self.createWorkout(request.user, request.data['name'])
#         self.createWorkoutExercises(createdWorkout, request.data['exercises'])
#         return Response("created workout")

#     def createWorkout(self, user, name):
#         newWorkout = Workout(user=user, name=name)
#         newWorkout.save()
#         return newWorkout

#     def createWorkoutExercises(self, workout, exercises):
#         for exercise in exercises:
#             exerciseInstance = Exercise.objects.get(id=exercise['exercise']['id'])

#             workoutExerciseInstance = WorkoutExercise(workout=workout, exercise=exerciseInstance, order=exercise['order'])
#             workoutExerciseInstance.save()

#             sets = []
#             for set in exercise['sets']:
#                 print(set)
#                 new_set = Set(workout_exercise=workoutExerciseInstance, description=set["description"], set_number=set["setNumber"], reps=set["reps"])
#                 sets.append(new_set)

#             Set.objects.bulk_create(sets)


           









