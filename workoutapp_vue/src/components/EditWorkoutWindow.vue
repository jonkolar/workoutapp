<template>
<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Edit Workout</h5>
          <span>
            <i class="bi bi-x-square" @click="closeWindow"></i>
          </span>
      </div>
      <div class="modal-body">

        <button @click="devShowExercises()">Dev Show Exercises</button>

        <form>
            <div class="m-3">
                <label for="workout-name" class="form-label" placeholder="Enter your workout name...">Workout Name:</label>
                <input type="text" v-model="currentWorkoutName" class="form-control" id="workout-name" required>
            </div>

            <ExerciseInputGroup v-for="userExercise in userExercises"
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
            <button type="button" class="btn btn-primary" @click="editWorkout">Save Changes</button>
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
    name: 'EditWorkoutWindow',
    components: {
        ExerciseInputGroup
    },
    props: ['userWorkoutId', 'currentUserExercises', 'currentWorkoutName'],
    emits: ['editWorkoutEmit', 'closeWindowEmit'],
    data() {
      return {
          workoutName: "",
          userExercises: [],
          errors: [],
      }
    },
    mounted() {
        this.fillCurrentWorkoutData()
    },
    methods: {
        closeWindow() {
            this.$emit('closeWindowEmit')
        },
        fillCurrentWorkoutData() {
            for(let i=0; i<this.currentUserExercises.length; i++) {
                this.userExercises.push({
                    userExerciseId: this.currentUserExercises[i].id,
                    exerciseId: this.currentUserExercises[i].exercise.id,
                    order: this.currentUserExercises[i].order,
                    description: this.currentUserExercises[i].description
                })
            }
        },
        addExercise() {
            this.userExercises.push({
                exerciseId: -1,
                order: this.userExercises.length + 1,
                description: "",
            })
        },
        editWorkout() {
            axios.post('/api/dashboard/workouts/update', {
                userWorkoutId: this.userWorkoutId,
                name: this.currentWorkoutName,
                userExercises: this.userExercises
            })
            .then((response) => {
                this.$emit('editWorkoutEmit')
                this.$emit('closeWindowEmit')
            })
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