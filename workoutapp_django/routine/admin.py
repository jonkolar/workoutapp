from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise, Set, Category

# Register your models here.
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(Exercise)
admin.site.register(Category)
admin.site.register(Set)
