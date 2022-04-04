<template>
    <div class="m-3 p-3 bg-light">
        <div class="d-flex justify-content-between">
            <h6 class="align-self-center">Exercise {{currentExercise}}:</h6>
            <i class="pointerButton bi bi-trash-fill" style="font-size: 20px; color: red;" 
                @click="$emit('removeExerciseEmit', currentExercise)">
            </i>
        </div>
        <div class="m-2">
            <label for="workout-exercise-select">Exercise:</label>
            <select class="form-select" :id="'workout-exercise-select' + currentExercise" required
                :model="exerciseId" @change="$emit('update:exerciseId', $event.target.value)" :value="exerciseId">
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

// TODO: Make getAllExercise 1 API call.

export default {
    name: 'ExerciseInputGroup',
    props: ['description', 'order', 'exerciseId', 'currentExercise', 'exerciseOptions'],
    emits: ['update:description', 'update:order', 'update:exerciseId', 'removeExerciseEmit'],
}
</script>