<template>

  <div class="card m-2 h-auto align-self-start" style="width: 18rem;">
    <div class="card-header table-responsive">
      <h4 class="m-1">
        {{routine.name}}

        <i v-if="!routine.is_private"
           class="bi bi-eye-fill ms-1"
           data-bs-toggle="tooltip"
           data-bs-placement="right"
           title="Public routine"
           v-tooltip></i>

        <i v-else
           class="bi bi-eye-slash-fill"
           data-bs-toggle="tooltip"
           data-bs-placement="right"
           title="Private routine"
           v-tooltip></i>
      </h4> 
      <span class="badge bg-dark ms-1" v-bind="category.id" v-for="category in routine.categories" :key="category.id">{{category.name}}</span>
    </div>
    <small v-if="routine.user_workouts.length <= 0" class="text-black-50 fst-italic">No Workouts</small>
    <ul v-else class="list-group list-group-flush">
      <li class="list-group-item" v-for="workout in routine.user_workouts" :key="workout.id">{{workout.name}}</li>
    </ul>
  </div>

</template>




<script>
export default {
    name: 'RoutineCard',
    props: {
        routine: Object
    }
}
</script>