<template>
  <div>
    <h1>{{routine.name}}</h1>
    <p>By: {{routine.user.username}}</p>
  </div>

  <WorkoutCard v-for="userWorkout in routine.user_workouts" :key="userWorkout.id"
               :workout="userWorkout" />

  <div v-if="$store.state.isAuthenticated && isRoutineOwner($store.state.accessToken)" class="mt-4">
    <i class="bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click=""></i>
  </div>


</template>

<script>
import axios from 'axios'
import WorkoutCard from '@/components/WorkoutCard'
import jwt_decode from "jwt-decode";

export default {
  name: 'Routine',
  components: {
    WorkoutCard
  },
  data () {
      return {
        routine: {
          user: {
            username: "",
            id: 1
          },
          user_workouts: []
        },
  
      }
  },
  mounted() {
      this.fetchRoutineData()
  },
  methods: {
    async fetchRoutineData() {
      this.$root.toggleIsLoading(true)

      await axios.get(`/api/public/routines/${this.$route.params.id}`)
          .then((response) => {
            this.routine = response.data
          })
      this.$root.toggleIsLoading(false)
    },
    isRoutineOwner(accessToken) {
      let authenticatedUser = jwt_decode(accessToken)
      return authenticatedUser.user_id === this.routine.id
    }
  }
}
</script>