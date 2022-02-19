<template>
<h4>Set {{ setNumber}}:</h4>
<div class="d-flex flex-row">
  <div>
    <label for="reps">Reps:</label>
    <input class="form-control" type="text" id="reps" @change="updateReps" v-model="reps" >
    <br>
    <label for="description">Description:</label>
    <input class="form-control" type="text" id="description" @change="updateDescription" v-model="description" >
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
    emits: ["updateSetReps", "updateSetDescription"],
    data() {
      return {
        reps: 0,
        description: ""
      }
    },
    methods: {
      updateReps(){
        this.$emit('updateSetReps', this.setNumber, this.reps)
      },
      updateDescription(){
        this.$emit('updateSetDescription', this.setNumber, this.description)
      }
    }
}
</script>