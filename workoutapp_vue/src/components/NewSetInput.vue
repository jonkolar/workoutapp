<template>
<h4>Set {{ setNumber }}:</h4>
<div class="d-flex flex-row">
  <div>
    <label for="reps">Reps:</label>
    <input class="form-control" type="text" v-model="reps" id="reps" >
    <br>
    <label for="description">Description:</label>
    <input class="form-control" type="text" v-model="description" id="description">
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
        description: String,
        reps: Number
    },
    data() {
      return {
        
      }
    },
    mounted() {

    }
}
</script>