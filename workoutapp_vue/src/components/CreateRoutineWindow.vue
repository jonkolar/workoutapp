<template>

<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">New Routine</h5>
          <span>
            <i class="bi bi-x-square" @click="$emit('toggleWindow', false)"></i>
          </span>
      </div>
      <div class="modal-body">

        <form>
            <label for="routine-category-select">Category Options:</label>
            <select class="form-select" id="routine-category-select" required @change="addSelectedCategory($event)">
                <option value="default" selected hidden>select a category to add...</option>
                <option v-for="category in routineCategoryOptions" :value="category.name">
                    {{ category.name }}
                </option>
            </select>
            <div id="selected-categories" class="mt-2">
                <span class="badge bg-dark ms-1" v-for="category in selectedRoutineCategories">{{ category }}</span>
            </div>
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

export default {
    name: 'CreateRoutineWindow',
    emits: ['toggleWindow'],
    data() {
      return {
          routineCategoryOptions: [],
          selectedRoutineCategories: []
      }
    },
    mounted() {
        this.getAllCategoryOptions()
    },
    methods: {
        getAllCategoryOptions() {
            axios.get('/api/public/routines/categories/all')
                .then((response) => {
                    for(let i = 0; i < response.data.length; i++){
                        this.routineCategoryOptions.push(response.data[i])
                    }
                })
        },
        addSelectedCategory(event) {
            if (!this.selectedRoutineCategories.includes(event.target.value)) {
                this.selectedRoutineCategories.push(event.target.value)
            }
            $("#routine-category-select").val("default")
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