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
          
      }
    },
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