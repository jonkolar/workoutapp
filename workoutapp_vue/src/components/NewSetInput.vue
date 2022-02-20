<template>
<h4>Set {{ setNumber }}:</h4>
<div class="d-flex flex-row">
  <div>
    <label for="reps">Reps:</label>
    <input class="form-control" type="text" id="reps" :value="reps" @input="$emit('update:reps', $event.target.value)" >
    <br>
    <label for="description">Description:</label>
    <input class="form-control" type="text" id="description" :value="description" @input="$emit('update:description', $event.target.value)" >
   </div>
</div>
<br>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddSetInput',
    props: ['setNumber', 'reps', 'description'],
    emits: ['update:reps', 'update:description'],
}

</script>