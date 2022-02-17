<template>
<h3>Set {{ setNumber }}:</h3>
<div class="d-flex flex-row">
  <div>
    <label for="repsSelect">Reps</label>
    <select class="form-select" id="repsSelect">
    </select>
    <br>
    <label for="description">Description</label>
    <input class="form-control" type="text" placeholder="Description" id="description">
   </div>
</div>


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
        // Populate Reps Dropdown with 1-99
        for(let i = 1; i < 100; i++){
              $('#repsSelect').append($('<option>', {
                text: i,
                value: i
               }))}
        $('#repsSelect').val(this.reps)
    }
}
</script>