from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Workout
from .serializers import WorkoutSerializer

# Create your views here.
class WorkoutDetail(APIView):
    def get(self, request):
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout, many=True)
        print(serializer.data)
        return Response(serializer.data)
