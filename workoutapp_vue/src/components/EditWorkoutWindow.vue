<template>
<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog modal-dialog-scrollable" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Edit Workout</h5>
          <span>
            <i class="bi bi-x-square" @click="closeWindow"></i>
          </span>
      </div>     
    <div class="modal-body" id="edit-workout-window-body">
        <form>
            <div class="m-3">
                <label for="workout-name" class="form-label" placeholder="Enter your workout name...">Workout Name:</label>
                <input type="text" v-model="currentWorkoutName" class="form-control" id="workout-name" required>
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
    props: ['userWorkoutId', 'currentUserExercises', 'currentWorkoutName', 'setConfirmWindow'],
    emits: ['editWorkoutEmit', 'closeWindowEmit'],
    data() {
      return {
          userExercises: [],
          errors: [],
          exerciseOptions: []
      }
    },
    mounted() {
        this.$root.toggleIsModalOpen(true)
        this.fillCurrentWorkoutData()
        this.getAllExerciseOptions()
    },
    methods: {
        closeWindow() {
            $('.modal-body').css('overflow', 'hidden');
            this.setConfirmWindow("Discard Changes?", "Any made changes will not be saved", "Discard", (answer) => {
                if (answer) {
                    this.$root.toggleIsModalOpen(false)
                    this.$emit('closeWindowEmit')
                } else {
                    $('.modal-body').css('overflow', 'auto');
                }
            })
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
            axios.put('/api/dashboard/workouts/update', {
                userWorkoutId: this.userWorkoutId,
                name: this.currentWorkoutName,
                userExercises: this.userExercises
            })
            .then((response) => {
                this.$emit('editWorkoutEmit')
                this.$emit('closeWindowEmit')
            })
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