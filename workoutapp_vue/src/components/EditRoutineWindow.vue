<template>
<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Edit Routine</h5>
          <span>
            <i class="bi bi-x-square" @click="closeWindow"></i>
          </span>
      </div>
      <div class="modal-body">

        <form>
            <div class="m-3">
                <label for="routine-name" class="form-label" placeholder="Enter your routine name...">Name:</label>
                <input type="text" v-model="routineName" class="form-control" id="routine-name" required>
            </div>

            <div class="m-3">
                <label for="routine-category-select">Category Options:</label>
                <select class="form-select" id="routine-category-select" required @change="addSelectedCategory($event)">
                    <option value="default" selected hidden>select a category to add...</option>
                    <option v-for="category in routineCategoryOptions" :key="category.id" :value="category.name">
                        {{ category.name }}
                    </option>
                </select>
                <div id="selected-categories" class="mt-2">
                    <div class="badge bg-dark ms-1" v-for="category in selectedRoutineCategories" :key="category.id">
                    {{ category }}
                    <i class="bi bi-x" @click="removeSelectedCategory(category)"></i>
                    </div>
                </div>
            </div>
        </form>

        <div class="form-check form-switch m-3 d-flex">
            <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="isPrivate">
            <label class="form-check-label checkbox-inline ms-2" for="flexSwitchCheckDefault">Private</label>

            <i  class="bi bi-info-circle-fill ms-1"
                data-bs-toggle="tooltip"
                data-bs-placement="right"
                title="Private routines will only be viewable by you"
                v-tooltip>
            </i>           
        </div>

        <div class="alert alert-danger p-1 m-3" role="alert" v-for="error in errors" :key="error"> {{error}} </div>

        <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="editRoutine">Save Changes</button>
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

export default {
    name: 'EditRoutineWindow',
    props: ['routine', 'setConfirmWindow'],
    emit: ['closeWindowEmit', 'updateRoutineEmit'],
    data() {
      return {
          routineName: "",
          isPrivate: false,
          routineCategoryOptions: [],
          selectedRoutineCategories: [],
          errors: [],
      }
    },
    mounted() {
        this.fillCurrentRoutineData(this.routine)
        this.getAllCategoryOptions()
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
        editRoutine() {
            this.errors = []

            if (this.routineName == "") { this.errors.push("Routine must have a name" ) }
            if (this.selectedRoutineCategories.length <= 0) { this.errors.push("Routine must have at least 1 category" ) }

            if (this.errors.length <= 0) { // No Errors
                axios.put('/api/dashboard/routines/update', {
                    routineId: this.routine.id,
                    routineName: this.routineName,
                    isPrivate: this.isPrivate,
                    routineCategories: this.selectedRoutineCategories
                })
                .then((response) => {
                    this.$emit('updateRoutineEmit')
                    this.$emit('closeWindowEmit')
                })
            }
        },
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
        },
        removeSelectedCategory(deletedCategory) {
            this.selectedRoutineCategories.splice(this.selectedRoutineCategories.indexOf(deletedCategory), 1)
        },
        fillCurrentRoutineData(routine) {
            this.routineName = this.routine.name
            this.isPrivate = this.routine.is_private

            routine.categories.forEach((category, index) => {
                this.selectedRoutineCategories.push(category.name)
            });
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