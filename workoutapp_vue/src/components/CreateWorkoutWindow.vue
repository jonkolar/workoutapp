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

        <form>
            <div class="m-3">
                <label for="workout-name" class="form-label" placeholder="Enter your workout name...">Name:</label>
                <input type="text" v-model="workoutName" class="form-control" id="workout-name" required>
            </div>
        </form>

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

export default {
    name: 'CreateWorkouteWindow',
    props: ['routineId'],
    emits: ['createWorkoutEmit'],
    data() {
      return {
          workoutName: "",
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
        createWorkout() {
            axios.post('/api/dashboard/workouts/create', {
                    routineId: this.routineId,
                    workoutName: this.workoutName,
                    workoutCategories: this.selectedWorkoutCategories
                })
                .then((response) => {
                    this.$emit('createWorkoutEmit')
                    this.toggleShowWindow()
                })
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