<template>


<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Exercise</h5>
          <span>
            <i class="bi bi-x-square" @click="$emit('toggleWindow', false)"></i>
          </span>
      </div>
      <div class="modal-body">

        <button type="button" class="btn btn-dark" @click="checkSetsDev">DEV CHECK SETS CONSOLE</button>

        <form class="w-50 p-3 mx-auto" @submit.prevent="submitExercise">
          <label for="categorySelect">Category:</label>
          <select class="form-select" id="categorySelect" @change="updateExerciseOptions($event.target.value)" v-model="selectedCategory" required>
            <option value="" selected hidden>choose a category...</option>
            <option v-for="category in categoryOptions" :value="category.id">
              {{ category.name }}
            </option>
          </select>
          <br>
          <label for="exerciseSelect">Exercise:</label>
          <select class="form-select" id="exerciseSelect" v-model="selectedExercise" :disabled="selectedCategory == ''" required>
            <option value="" selected hidden>choose an exercise...</option>
            <option v-for="exercise in exerciseOptions" :value="exercise.id">
              {{ exercise.name }}
            </option>
          </select>
          <br>
          <label for="orderSelect">Order</label>
          <select class="form-select" id="orderSelect" v-model="order">
            <option v-for="index in 100" :value="index">
              {{index}}
            </option>
          </select>
          <br>

          <NewSetInput
            v-for="set in sets"
            v-model:setNumber="set.setNumber"
            v-model:reps="set.reps" 
            v-model:description="set.description" />

          <button type="button" class="btn btn-dark" @click="addSet">Add Set</button>

        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" @click="submitExercise">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="$emit('toggleWindow', false)">Close</button>
      </div>
    </div>
  </div>
  <br>
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
    emits: ['toggleWindow', 'addExercise'],
    data() {
      return {
        categoryOptions: [],
        exerciseOptions: [],
        selectedCategory: "",
        selectedExercise: "",
        isPrivate: false,
        order: 1,
        sets: []
      }
    },
    mounted() {
      // Populate Categories
      axios.get('/api/workouts/categorys/all')
      .then((response) => {
        for(let i = 0; i < response.data.length; i++){
          this.categoryOptions.push({
            id: response.data[i].id,
            name: response.data[i].name
          })
        }
      })
    },
    methods: {
        addExercise() {
            this.$emit('addExercise', {
              category: this.category,
              exercise: this.exercise,
              order: this.order,
              sets: this.sets
            })
        },
        updateExerciseOptions(categoryId) {
          this.exerciseOptions = []
          axios.get(`/api/workout/exercises/${categoryId}`)
              .then((response) => {
                for(let i = 0; i < response.data.length; i++){
                  this.exerciseOptions.push({
                    id: response.data[i].id,
                    name: response.data[i].name
                  })
                }
              })
       },
       addSet() {
         this.sets.push({
           setNumber: this.sets.length + 1,
           reps: 1,
           description: ""
         })
       },
       checkSetsDev() { // For Testing
         console.log(this.sets)
       },
       submitExercise() {
         let newExercise = {
           category: this.categoryOptions.find(category => category.id == this.selectedCategory),
           exercise: this.exerciseOptions.find(exercise => exercise.id == this.selectedExercise),
           order: this.order,
           sets: this.sets
         }

         this.$emit('addExercise', newExercise)
         this.$emit('toggleWindow', false)

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