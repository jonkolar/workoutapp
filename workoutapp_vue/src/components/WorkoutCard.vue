<template>
  <div class="bg-light mt-5  p-3">
  <div class="container d-flex flex-column align-items-center">
    <h3>{{workout.name}}</h3>      
    
    <ol class="exercise-list list-group list-group-numbered">
      <li class="exercise-list-item list-group-item d-flex justify-content-between align-items-start" v-for="userExercise in workout.user_exercises">
        <div class="ms-2 me-auto">
          <div class="fw-bold">{{userExercise.exercise.name}}</div>
          <p class="m-0">{{userExercise.description}}</p>
        </div>
        <span class="badge bg-dark ms-1" v-for="category in userExercise.exercise.categories" :key="category.id">{{category.name}}</span>
      </li>
    </ol>
    <div v-if="isOwner" id="workout-edit-options" class="mt-3">

      <EditWorkoutWindow v-if="showEditWorkoutWindow"
        @closeWindowEmit="toggleEditWorkoutWindow"
        @editWorkoutEmit="workoutEdited"
        :userWorkoutId="workout.id"
        :currentWorkoutName="workout.name"
        :currentUserExercises="workout.user_exercises" />

      <i class="pointerButton bi bi-gear-fill ms-2" style="font-size: 20px" @click="toggleEditWorkoutWindow"></i>
      <i class="pointerButton bi bi-trash-fill ms-2" style="font-size: 20px; color: red;"></i>
    </div>
  </div>
</div>
</template>
<script>
import EditWorkoutWindow from '@/components/EditWorkoutWindow'

export default {
    name: 'WorkoutCard',
    components: {
      EditWorkoutWindow
    },
    props: ['workout', 'isOwner', 'workoutEdited'],
    data() {
      return {
        showEditWorkoutWindow: false
      }
    },
    methods: {
      toggleEditWorkoutWindow() {
        this.showEditWorkoutWindow = !this.showEditWorkoutWindow
      }
    }
}
</script>

<style scoped>
  .exercise-list {
    width: 90%;
    max-width: 500px;
  }

  .exercise-list-item {
    text-align: left;
  }
</style>