from cgitb import reset
from email.errors import CloseBoundaryNotFoundDefect
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
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


class UpdateUserRoutine(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        routine_id = request.data["routineId"]
        updated_routine_name = request.data["routineName"]
        updated_routine_categories = request.data["routineCategories"]
        updated_routine_isPrivate = request.data["isPrivate"]

        routine = UserRoutine.objects.get(pk=routine_id)

        # Update Name
        if updated_routine_name != routine.name:
            routine.name = updated_routine_name
        
        # Update isPrivate
        if updated_routine_isPrivate != routine.is_private:
            routine.is_private = updated_routine_isPrivate

        # Check Update Categories
        categories_to_add = []
        categories_that_exist = []
        categories_to_delete = []

        current_categories = routine.categories.all()
        for updated_category in updated_routine_categories:
            updated_routine_category = RoutineCategory.objects.get(name=updated_category)
            if updated_routine_category not in current_categories:
                categories_to_add.append(updated_routine_category)
            else:
                categories_that_exist.append(updated_routine_category)

        for category in current_categories:
            if category not in categories_that_exist and category not in categories_to_add:
                categories_to_delete.append(category)   
        
        # Add Categories
        for category in categories_to_add:
            routine.categories.add(category)

        # Delete Categories
        for category in categories_to_delete:
            routine.categories.remove(category)

        routine.save()


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


class DeleteUserWorkout(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        user_workout_id = request.data["userWorkoutId"]
        UserWorkout.objects.filter(id=user_workout_id).delete()
        return Response("Workout Deleted")


class UpdateUserWorkout(APIView):
    authentication_Classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        id = request.data["userWorkoutId"]
        updated_name = request.data["name"]
        updated_user_exercises = request.data["userExercises"]

        # Update User Workout Fields
        user_workout = UserWorkout.objects.get(pk=id)
        if user_workout.name != updated_name:
            user_workout.name = updated_name
            user_workout.save()

        # Update User Exercise Fields
        user_exercises = UserExercise.objects.filter(workout_id=id)
        for updated_user_exercise in updated_user_exercises:
            if 'userExerciseId' in updated_user_exercise:
                for user_exercise in user_exercises:
                    if updated_user_exercise['userExerciseId'] == user_exercise.id:
                        write_fields(user_exercise, 
                        description=updated_user_exercise["description"],
                        order=updated_user_exercise["order"],
                        exercise_id=updated_user_exercise["exerciseId"])
                        updated = True
                        break
            else: # Add New User Exercise
                exercise = Exercise.objects.get(pk=updated_user_exercise['exerciseId'])
                user_workout.user_exercises.create(exercise=exercise, order=updated_user_exercise['order'], 
                                                    description=updated_user_exercise['description'])
                
        return Response("User Workout Updated")

# Helper methods:

def write_fields(obj, **kwargs):
        should_save = False
        
        for k, v in kwargs.items():
            if getattr(obj, k) != v:
                setattr(obj, k, v)
                should_save = True

        if should_save:
            obj.save(update_fields=kwargs.keys())



           









