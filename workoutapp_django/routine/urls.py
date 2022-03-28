from django.urls import path, include
from routine.views import dashboard_views, public_views

urlpatterns = [
    path('dashboard/routines/all', dashboard_views.GetAllUserRoutines.as_view()),
    path('dashboard/routines/create', dashboard_views.CreateUserRoutine.as_view()),
    path('dashboard/routines/update', dashboard_views.UpdateUserRoutine.as_view()),
    path('dashboard/routines/delete', dashboard_views.DeleteUserRoutine.as_view()),
    path('dashboard/workouts/create', dashboard_views.CreateUserWorkout.as_view()),
    path('dashboard/workouts/update', dashboard_views.UpdateUserWorkout.as_view()),
    path('dashboard/workouts/delete', dashboard_views.DeleteUserWorkout.as_view()),
    
    path('public/routines/categories/all', public_views.GetAllRoutineCategories.as_view()),
    path('public/routines/<int:id>', public_views.GetUserRoutine.as_view()),

    path('public/workouts/categories/all', public_views.GetAllWorkoutCategories.as_view()),
    path('public/workouts/exercises/all', public_views.GetAllExercises.as_view())
]