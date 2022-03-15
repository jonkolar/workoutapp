<template>
<div class="mt-4">
    <i class="bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click="toggleShowWindow"></i>
</div>

<div v-if="showWindow" class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Workout</h5>
          <span>
            <i class="bi bi-x-square" @click="toggleShowWindow"></i>
          </span>
      </div>
      <div class="modal-body">

        <button @click="devShowExercises()">Dev Show Exercises</button>

        <form>
            <div class="m-3">
                <label for="workout-name" class="form-label" placeholder="Enter your workout name...">Workout Name:</label>
                <input type="text" v-model="workoutName" class="form-control" id="workout-name" required>
            </div>

            <AddExerciseInputGroup v-for="userExercise in userExercises"
                :currentExercise="userExercises.indexOf(userExercise) + 1"
                v-model:description="userExercise.description"
                v-model:order="userExercise.order"
                v-model:exerciseId="userExercise.exerciseId" />

        </form>

        <div>
            <i class="bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click="addExercise"></i>
        </div>

        <div class="alert alert-danger p-1 m-3" role="alert" v-for="error in errors" :key="error"> {{error}} </div>

        <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="createWorkout">Create Workout</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="toggleShowWindow">Close</button>
        </div>

      </div>

    </div>
  </div>
  <br>
</div>


</template>

<script>
import axios from 'axios'
import AddExerciseInputGroup from '@/components/AddExerciseInputGroup'

export default {
    name: 'CreateWorkouteWindow',
    components: {
        AddExerciseInputGroup
    },
    props: ['routineId'],
    emits: ['createWorkoutEmit'],
    data() {
      return {
          workoutName: "",
          userExercises: [],
          errors: [],
          showWindow: false
      }
    },
    mounted() {
        
    },
    methods: {
        toggleShowWindow() {
            this.showWindow = !this.showWindow
        },
        addExercise() {
            this.userExercises.push({
                exerciseId: -1,
                order: this.userExercises.length + 1,
                description: "",
            })
        },
        createWorkout() {
            this.errors = []

            if (this.workoutName == "") { this.errors.push("Workout must have a name" ) }

            if (this.errors.length <= 0) { // No Errors
                axios.post('/api/dashboard/workouts/create', {
                    routineId: this.routineId,
                    workoutName: this.workoutName,
                    userExercises: this.userExercises
                })
                .then((response) => {
                    // do something
                })
            }
        },
        devShowExercises() {
            console.log(this.userExercises)
        }
    }
}
</script>

<style>
    .modal {
        display: flex;
        background-color: rgb(0, 0, 0, 0.5)
    }

    .modal-backdrop {
        background-color: red;
    }

    .modal-dialog {
        width: 90%;
        max-width: 500px;
    }
</style>