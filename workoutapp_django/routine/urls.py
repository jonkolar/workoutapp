from django.urls import path, include
from routine import views

urlpatterns = [
    path('workouts/<str:username>/<int:workout_id>/', views.GetUserWorkouts),
    path('workouts/user/all', views.GetAllUserWorkouts.as_view()),
    path('workouts/categorys/all', views.GetAllCategories.as_view()),
    path('workout/exercises/<str:category>', views.GetExercises.as_view())
]