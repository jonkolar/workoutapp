from django.db.models import Q
from django.http import Http404
from users.models import CustomUser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Workout
from .serializers import WorkoutSerializer

# Create your views here.
class WorkoutDetail(APIView):
    def get(self, request, username, workout_id):
        user = CustomUser.objects.get(username=username)
        workout = Workout.objects.get(user_id=user.id)
        workout_serialized = WorkoutSerializer(workout)
        return Response(workout_serialized.data)
