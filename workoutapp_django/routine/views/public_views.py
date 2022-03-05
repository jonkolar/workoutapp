from users.models import CustomUser

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import RoutineCategory, UserRoutine, WorkoutCategory, UserWorkout, Exercise, UserExercise
from ..serializers import RoutineCategorySerializer, UserRoutineSerializer

class GetAllCategories(APIView):
    def get(self, request):
        all_categories = RoutineCategory.objects.all()
        all_categories_serialized = RoutineCategorySerializer(all_categories, many=True)
        return Response(all_categories_serialized.data)