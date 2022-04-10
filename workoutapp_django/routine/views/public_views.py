from msilib.schema import Error, ListView
from users.models import CustomUser
from django.core.paginator import Paginator

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import RoutineCategory, UserRoutine, ExerciseCategory, UserWorkout, Exercise, UserExercise
from ..serializers import ExerciseSerializer, RoutineCategorySerializer, UserRoutineSerializer, ExerciseCategorySerializer


class GetAllUserRoutines(APIView):
    def get(self, request, page):
        all_user_routines = UserRoutine.objects.filter(is_private=False).order_by('-id') # Only Show Non Private Routines
        paginator = Paginator(all_user_routines, 2)

        page_obj = paginator.get_page(page)
        page_routines_serialized = UserRoutineSerializer(page_obj.object_list, many=True)
        return Response({"routines": page_routines_serialized.data, "has_more": page_obj.has_next()})

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
        all_categories = ExerciseCategory.objects.all()
        all_categories_serialized = ExerciseCategorySerializer(all_categories, many=True)
        return Response(all_categories_serialized.data)

class GetAllExercises(APIView):
    def get(self, request):
        all_exercises = Exercise.objects.all()
        all_exercises_serialiazed = ExerciseSerializer(all_exercises, many=True)
        return Response(all_exercises_serialiazed.data)