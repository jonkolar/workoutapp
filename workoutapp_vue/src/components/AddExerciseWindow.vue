<template>


<div class="modal" tabindex="1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
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
export default {
    name: 'AddExerciseWindow',
    methods: {
        close () {
            this.$emit('closeAddExerciseWindow', false)
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