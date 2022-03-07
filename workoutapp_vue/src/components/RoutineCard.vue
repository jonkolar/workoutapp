<template>

  <div class="card m-2 h-auto" style="width: 18rem;">
    <div class="card-header table-responsive">
      <h4 class="m-1">
        {{routine.name}}
        <i v-if="!routine.is_private" class="bi bi-eye-fill ms-1"></i>
        <i v-else class="bi bi-eye-slash-fill"></i>
      </h4> 
      <span class="badge bg-dark ms-1" v-bind="category.id" v-for="category in routine.categories" :key="category.id">{{category.name}}</span>
    </div>
    <ul class="list-group list-group-flush">
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