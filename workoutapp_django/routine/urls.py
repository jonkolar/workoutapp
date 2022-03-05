from django.urls import path, include
from routine.views import dashboard_views, public_views

urlpatterns = [
    path('dashboard/routines/all', dashboard_views.GetAllUserRoutines.as_view()),
    
    path('public/routines/categories/all', public_views.GetAllCategories.as_view())
    # path('workouts/user/all', views.GetAllUserWorkouts.as_view()),
    # path('workouts/categorys/all', views.GetAllCategories.as_view()),
    # path('workout/exercises/<str:category>', views.GetExercises.as_view()),
    # path('workout/create', views.CreateWorkout.as_view(),)
]