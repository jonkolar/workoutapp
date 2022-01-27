from django.urls import path, include
from routine import views

urlpatterns = [
    path('workout/', views.WorkoutDetail.as_view()),
]