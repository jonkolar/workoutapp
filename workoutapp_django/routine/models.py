from django.db import models

from django.contrib.auth import get_user_model
CustomUser = get_user_model()

# Create your models here.

class RoutineCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class UserRoutine(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ManyToManyField(RoutineCategory, related_name="categories")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name="user")
    is_private = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

class WorkoutCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class UserWorkout(models.Model):
    routine = models.ForeignKey(UserRoutine, on_delete=models.CASCADE, default=1, related_name="user_workouts")
    categories = models.ManyToManyField(WorkoutCategory)
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=150, unique=True)
    categories = models.ManyToManyField(WorkoutCategory, related_name="routines")

    def __str__(self):
        return self.name

class UserExercise(models.Model):
    workout = models.ForeignKey(UserWorkout, on_delete=models.CASCADE, default=1, related_name="workout")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, default=1, related_name="user_exercises")
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.workout.routine.user.username + ": " + self.workout.name + ": " + self.exercise.name


# class Category(models.Model):
#     name = models.CharField(max_length=150, unique=True)
    
#     def __str__(self):
#         return self.name

# class Exercise(models.Model):
#     name = models.CharField(max_length=150, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Workout(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name="user")
#     name = models.CharField(max_length=150)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class WorkoutExercise(models.Model):
#     workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
#     order = models.IntegerField(default=1)
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.workout.name + ": " + self.exercise.name

# class Set(models.Model):
#     workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name="sets")
#     description = models.CharField(max_length=250)
#     set_number = models.IntegerField()
#     reps = models.IntegerField()

#     def __str__(self):
#         return self.workout_exercise.workout.name + ": " + self.workout_exercise.exercise.name + ": " + self.description + ": " + str(self.set_number) + ": " + str(self.reps)
