from msilib.schema import Error
from users.models import CustomUser

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import RoutineCategory, UserRoutine, WorkoutCategory, UserWorkout, Exercise, UserExercise
from ..serializers import RoutineCategorySerializer, UserRoutineSerializer, WorkoutCategorySerializer

class GetAllRoutineCategories(APIView):
    def get(self, request):
        all_categories = RoutineCategory.objects.all()
        all_categories_serialized = RoutineCategorySerializer(all_categories, many=True)
        return Response(all_categories_serialized.data)

class GetUserRoutine(APIView):
    def get(self, request, id):
        routine = UserRoutine.objects.get(pk=id)
        print(request.user.id)
        print(id)
        if routine.is_private and not request.user.id == routine.user.id:
            return Response("Private Routine")

        routine_serialized = UserRoutineSerializer(routine)
        
        return Response(routine_serialized.data)

class GetAllWorkoutCategories(APIView):
    def get(self, request):
        all_categories = WorkoutCategory.objects.all()
        all_categories_serialized = WorkoutCategorySerializer(all_categories, many=True)
        return Response(all_categories_serialized.data)