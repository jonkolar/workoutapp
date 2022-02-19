<template>
<h4>Set {{ setNumber}}:</h4>
<div class="d-flex flex-row">
  <div>
    <label for="reps">Reps:</label>
    <input class="form-control" type="text" id="reps" @change="updateReps" v-model="reps" >
    <br>
    <label for="description">Description:</label>
    <input class="form-control" type="text" id="description">
   </div>
</div>
<br>
</template>


<script>
import axios from 'axios'

export default {
    name: 'AddSetInput',
    props: {
        setNumber: Number,
    },
    emits: ["updateSetReps"],
    data() {
      return {
        reps: 0
      }
    },
    methods: {
      updateReps(){
        this.$emit('updateSetReps', this.setNumber, this.reps)
      }
    }
}
</script>