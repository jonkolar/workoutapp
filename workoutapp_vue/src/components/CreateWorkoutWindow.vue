<template>
<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog modal-dialog-scrollable" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Workout</h5>
          <span>
            <i class="bi bi-x-square" @click="closeWindow"></i>
          </span>
      </div>
      <div class="modal-body">

        <button @click="devShowExercises()">Dev Show Exercises</button>

        <form>
            <div class="m-3">
                <label for="workout-name" class="form-label" placeholder="Enter your workout name...">Workout Name:</label>
                <input type="text" v-model="workoutName" class="form-control" id="workout-name" required>
            </div>

            <ExerciseInputGroup v-for="userExercise in userExercises"
                :currentExercise="userExercises.indexOf(userExercise) + 1"
                :exerciseOptions="exerciseOptions"
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
            <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="closeWindow">Close</button>
        </div>

      </div>

    </div>
  </div>
  <br>
</div>


</template>

<script>
import axios from 'axios'
import ExerciseInputGroup from '@/components/ExerciseInputGroup'

export default {
    name: 'CreateWorkoutWindow',
    components: {
        ExerciseInputGroup
    },
    props: ['routineId', 'setConfirmWindow'],
    emits: ['createWorkoutEmit', 'closeWindowEmit'],
    data() {
      return {
          workoutName: "",
          userExercises: [],
          errors: [],
          exerciseOptions: []
      }
    },
    mounted() {
        this.$root.toggleIsModalOpen(true)
        this.getAllExerciseOptions()
    },
    methods: {
        closeWindow() {
            $('.modal-body').css('overflow', 'hidden');
            this.setConfirmWindow("Discard New Workout", "New workout will not be saved and you will have to " +
                                    "start again from scratch", "Discard", (answer) => {
                if (answer) {
                    this.$root.toggleIsModalOpen(false)
                    this.$emit('closeWindowEmit')
                } else {
                    $('.modal-body').css('overflow', 'auto');
                }
            })
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
                    this.$emit('createWorkoutEmit')
                    this.$emit('closeWindowEmit')
                })
            }
        },
        getAllExerciseOptions() {
            axios.get('/api/public/workouts/exercises/all')
                .then((response) => {
                    for(let i = 0; i < response.data.length; i++){
                        this.exerciseOptions.push(response.data[i])
                    }
                })
        },
    }
}
</script>

<style>
    .modal {
        display: flex;
        background-color: rgb(0, 0, 0, 0.5);
    }

    .modal-backdrop {
        background-color: red;
    }

    .modal-dialog {
        width: 90%;
        max-width: 500px;
    }
</style>