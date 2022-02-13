<template>

  <div class="card m-2 h-auto" style="width: 18rem;">
    <div class="card-header table-responsive">
    {{workout.name}}
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item" v-for="exercise in workout.exercises">{{exercise.order}}. {{exercise.exercise}}</li>
    </ul>
  </div>

</template>




<script>
export default {
    name: 'WorkoutCard',
    props: {
        workout: Object
    }
}
</script>