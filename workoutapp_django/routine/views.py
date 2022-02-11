from users.models import CustomUser

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Workout
from .serializers import WorkoutSerializer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserWorkouts(request, username, workout_id):
    user = CustomUser.objects.get(username=username)
    workout = Workout.objects.get(user_id=user.id)
    workout_serialized = WorkoutSerializer(workout)
    return Response(workout_serialized.data)



