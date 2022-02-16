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
        <form class="w-50 p-3 mx-auto" @submit.prevent="submitLogin">
          <label for="categorySelect">Category:</label>
          <select class="form-select" id="categorySelect" @change="populateExercises">
          </select>
        </form>
        <form class="w-50 p-3 mx-auto" @submit.prevent="submitLogin">
          <label for="exerciseSelect">Exercise:</label>
          <select class="form-select" id="exerciseSelect">
            <option selected>Select a Category...</option>
          </select>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="close">Close</button>
      </div>
    </div>
  </div>
</div>


</template>


<script>
import axios from 'axios'

export default {
    name: 'AddExerciseWindow',
    data() {
      return {
        category: "",
        exercise: ""
      }
    },
    mounted() {
      // Populate Categories
      axios.get('/api/workouts/categorys/all')
          .then((response) => {
            for(let i = 0; i < response.data.length; i++){
              $('#categorySelect').append($('<option>', {
                value: response.data[i].id,
                text: response.data[i].name
              }));
            }
          })
    },
    methods: {
        close () {
            this.$emit('closeAddExerciseWindow', false)
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