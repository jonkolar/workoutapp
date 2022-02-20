<template>
 <div>
    <form class="w-50 p-3 mx-auto" @submit.prevent="submitLogin">
      <button type="button" class="btn btn-dark" @click="checkExercisesDev">DEV CHECK EXERCISES CONSOLE</button>
      <div class="mb-3">
        <label for="workout-name" class="form-label">Name:</label>
        <input type="text" v-model="name" class="form-control" id="workout-name" required>
      </div>
      <div>
        <i class="bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click="toggleAddExerciseWindow(true)"></i>
      </div>
      
      <div v-if="showAddExerciseWindow">
        <AddExerciseWindow 
            @toggleWindow="toggleAddExerciseWindow"
            @addExercise="addExercise" />
      </div>
    </form>

      <br>
      <br>
      <br>

    <button type="submit" class="btn btn-primary">Create Workout</button>
</div>
</template>

<script>
import axios from 'axios'
import AddExerciseWindow from '@/components/AddExerciseWindow'

export default {
  name: 'CreateWorkout',
  components: {
      AddExerciseWindow,
  },
  data () {
      return {
        name: "",
        exercises: [],
        showAddExerciseWindow: false,
      }
  },
  methods: {
      toggleAddExerciseWindow(bool) {
          this.showAddExerciseWindow = bool
      },
      addExercise(newExercise) {
        this.exercises.push(newExercise)
      },
      checkExercisesDev() { // For Testing
         console.log(this.exercises)
       }

  },
}
</script>