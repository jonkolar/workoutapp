from django.urls import path, include
from routine import views

urlpatterns = [
    path('routines/user/all', views.GetAllUserRoutines.as_view()),
    # path('workouts/user/all', views.GetAllUserWorkouts.as_view()),
    # path('workouts/categorys/all', views.GetAllCategories.as_view()),
    # path('workout/exercises/<str:category>', views.GetExercises.as_view()),

    # path('workout/create', views.CreateWorkout.as_view(),)
]