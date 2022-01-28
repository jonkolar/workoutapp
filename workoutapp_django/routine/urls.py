from django.urls import path, include
from routine import views

urlpatterns = [
    path('workout/<str:username>/<int:workout_id>/', views.WorkoutDetail.as_view()),
]