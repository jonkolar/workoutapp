<template>
  <div class="bg-light mt-5  p-3">
  <div class="container d-flex flex-column align-items-center">
    <h3>{{workout.name}}</h3>      
    
    <ol class="exercise-list list-group">
      <li class="exercise-list-item list-group-item d-flex justify-content-between align-items-start" v-for="userExercise in userExercisesSorted">
        <p>{{userExercise.order}}.</p>
        <div class="ms-2 me-auto">
          <div class="fw-bold">{{userExercise.exercise.name}}</div>
          <p class="m-0">{{userExercise.description}}</p>
        </div>
        <span class="badge bg-dark ms-1" v-for="category in userExercise.exercise.categories" :key="category.id">{{category.name}}</span>
      </li>
    </ol>
    <div v-if="isOwner" id="workout-edit-options" class="mt-3">

      <i class="pointerButton bi bi-gear-fill ms-2" style="font-size: 20px" 
        @click="setEditWorkoutWindowCurrentWorkout(workout)"></i>
      <i class="pointerButton bi bi-trash-fill ms-2" style="font-size: 20px; color: red;" 
        @click="destroyWorkout">
      </i>
    </div>
  </div>
</div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'WorkoutCard',
    props: ['workout', 'isOwner', 'setEditWorkoutWindowCurrentWorkout', 'setConfirmWindow'],
    emits: ['deletedWorkoutEmit'],
    computed: {
        userExercisesSorted: function() {
            return this.workout.user_exercises.sort((a, b) => a.order - b.order)
        }
    },
    methods: {
      destroyWorkout() {
            const deleteWorkoutCallback = (answer) => {
                this.$root.toggleIsModalOpen(false)
                if(answer){
                    axios.delete('/api/dashboard/workouts/delete', { data: {
                        userWorkoutId: this.workout.id
                    }})
                    .then((response) => {
                        this.$emit('closeWindowEmit')
                        this.$emit('deletedWorkoutEmit')
                    })
                }
            }

            this.setConfirmWindow("Delete Workout?", 
                                    "Once a workout is deleted it cannot be recovered." + 
                                    "Are you sure you'd like to delete this workout?",
                                    "Confirm Deletion", deleteWorkoutCallback)
                                    
        },
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