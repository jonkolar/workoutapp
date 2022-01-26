from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Set(models.Model):
    description = models.CharField(max_length=250)
    reps = models.IntegerField()

    def __str__(self):
        return self.description

class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set = models.ManyToManyField(Set)

    def __str__(self):
        return self.exercise.name

class Workout(models.Model):
    name = models.CharField(max_length=150)
    workout_exercise = models.ManyToManyField(WorkoutExercise)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
