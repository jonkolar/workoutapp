from django.contrib import admin
from .models import RoutineCategory, UserRoutine, WorkoutCategory, UserWorkout, Exercise, UserExercise

# Register your models here.
admin.site.register(RoutineCategory)
admin.site.register(UserRoutine)
admin.site.register(WorkoutCategory)
admin.site.register(UserWorkout)
admin.site.register(Exercise)
admin.site.register(UserExercise)
