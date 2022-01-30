from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name="user")
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    order = models.IntegerField(default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return self.workout.name + ": " + self.exercise.name

class Set(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name="sets")
    description = models.CharField(max_length=250)
    set_number = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.workout_exercise.workout.name + ": " + self.workout_exercise.exercise.name + ": " + self.description + ": " + str(self.set_number) + ": " + str(self.reps)
