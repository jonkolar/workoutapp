<template>
  <div class="bg-light mt-5  p-3">
  <div class="container d-flex flex-column align-items-center">
    <h3>{{workout.name}}</h3>      
    
    <ol class="exercise-list list-group list-group-numbered">
      <li class="exercise-list-item list-group-item d-flex justify-content-between align-items-start" v-for="userExercise in workout.user_exercises">
        <div class="ms-2 me-auto">
          <div class="fw-bold">{{userExercise.exercise.name}}</div>
          <p class="m-0">{{userExercise.description}}</p>
        </div>
        <span class="badge bg-dark ms-1" v-for="category in userExercise.exercise.categories" :key="category.id">{{category.name}}</span>
      </li>
    </ol> 
  </div>
</div>
</template>
<script>

export default {
    name: 'WorkoutCard',
    props: {
        workout: Object
    },
}
</script>

<style scoped>
  .exercise-list {
    width: 90%;
    max-width: 500px;
  }

  .exercise-list-item {
    text-align: left;
  }
</style>