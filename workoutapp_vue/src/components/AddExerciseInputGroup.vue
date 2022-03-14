<template>
    <div class="m-3 p-3 bg-light">
        <h5>Exercise {{currentExercise}}</h5>
        <div class="m-2">
            <label for="workout-exercise-select">Exercise:</label>
            <select class="form-select" id="workout-exercise-select" required
                @change="$emit('update:exerciseId', $event.target.value)">
                <option value="-1" selected hidden>select the exercise...</option>
                <option v-for="exercise in exerciseOptions" :key="exercise.id" :value="exercise.id">
                {{ exercise.name }}
                </option>
            </select>
        </div>
        <div class="m-2">
            <label for="workout-exercise-order" class="m-1">Order:</label>
            <br>
            <input :value="order" type="number" id="workout-exercise-order" min="1" max="1000" 
                @change="$emit('update:order', $event.target.value)">
        </div>
        <div class="m-2">
            <label for="workout-exercise-description" class="m-1">Description:</label>
            <textarea id="workout-exercise-description" style="width: 100%" 
                :value="description" @change="$emit('update:description', $event.target.value)"></textarea>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddExerciseInputGroup',
    props: ['description', 'order', 'exerciseId', 'currentExercise'],
    emits: ['update:description', 'update:order', 'update:exerciseId'],
    data() {
      return {
          exerciseOptions: [],
          errors: [],
      }
    },
    mounted() {
        this.getAllExerciseOptions()
    },
    methods: {
        getAllExerciseOptions() {
            axios.get('/api/public/workouts/exercises/all')
                .then((response) => {
                    for(let i = 0; i < response.data.length; i++){
                        this.exerciseOptions.push(response.data[i])
                    }
                })
        },
    }
}
</script>