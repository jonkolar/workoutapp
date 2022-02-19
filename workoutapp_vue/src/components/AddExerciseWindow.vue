<template>


<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Exercise</h5>
          <span>
            <i class="bi bi-x-square" @click="close"></i>
          </span>
      </div>
      <div class="modal-body">

        <button type="button" class="btn btn-dark" @click="checkSetsDev">DEV CHECK SETS CONSOLE</button>

        <form class="w-50 p-3 mx-auto" @submit.prevent="submitLogin">
          <label for="categorySelect">Category:</label>
          <select class="form-select" id="categorySelect" @change="populateExercises" v-model="category">
          </select>
          <br>
          <label for="exerciseSelect">Exercise:</label>
          <select class="form-select" id="exerciseSelect" v-model="exercise">
          </select>
          <br>
          <label for="orderSelect">Order</label>
          <select class="form-select" id="orderSelect">
          </select>
          <br>

          <NewSetInput
            v-for="set in sets"
            v-bind:setNumber="set.setNumber"
            @updateSetReps="updateSetReps" 
            @updateSetDescription="updateSetDescription" />

          <button type="button" class="btn btn-dark" @click="addSet">Add Set</button>

        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" @click="addExercise">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="close">Close</button>
      </div>
    </div>
  </div>
</div>


</template>


<script>
import axios from 'axios'
import NewSetInput from '@/components/NewSetInput'

export default {
    name: 'AddExerciseWindow',
    components: {
      NewSetInput,
    },
    data() {
      return {
        category: "",
        exercise: "",
        order: 0,
        sets: []
      }
    },
    mounted() {
      // Populate Categories
      axios.get('/api/workouts/categorys/all')
          .then((response) => {
            for(let i = 0; i < response.data.length; i++){
              if (i == 0) { this.category = response.data[i].id }
              $('#categorySelect').append($('<option>', {
                value: response.data[i].id,
                text: response.data[i].name
              }));
            }
          })

      // Populate Exercises
      axios.get(`/api/workout/exercises/1`)
            .then((response) => {
              for(let i = 0; i < response.data.length; i++){
                if (i == 1) { this.exercise = response.data[i].name }
                $('#exerciseSelect').append($('<option>', {
                  text: response.data[i].name
                }));
              }
            })
      
      // Populate Order Dropdown with 1-99
      for(let i = 1; i < 100; i++){
              $('#orderSelect').append($('<option>', {
                text: i,
                value: i
               }))}
    },
    methods: {
        close () {
            this.$emit('closeAddExerciseWindow', false)
        },
        addExercise() {
            this.$emit('addExercise', {
              category: this.category,
              exercise: this.exercise,
              order: this.order,
              sets: this.sets
            })
        },
        populateExercises() {
          let categoryID = $('#categorySelect').find(":selected").val()
          $('#exerciseSelect').empty()
          axios.get(`/api/workout/exercises/${categoryID}`)
              .then((response) => {
                for(let i = 0; i < response.data.length; i++){
                  $('#exerciseSelect').append($('<option>', {
                    text: response.data[i].name
                  }));
                }
              })
       },
       addSet() {
         this.sets.push({
           setNumber: this.sets.length + 1,
           reps: 0,
           description: ""
         })
       },
       updateSetReps(setNumber, newReps){
         this.sets[setNumber - 1].reps = newReps
       },
       updateSetDescription(setNumber, newDescription){
         this.sets[setNumber - 1].description = newDescription
       },
       checkSetsDev() {
         console.log(this.sets)
       }
    }
}
</script>

<style>
    .modal {
        display: block;
        background-color: rgb(0, 0, 0, 0.5)
    }

    .modal-backdrop {
        background-color: red;
    }
</style>