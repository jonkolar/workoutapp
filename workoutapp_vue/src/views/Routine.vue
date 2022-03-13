<template>
  <div>
    <h1>{{routine.name}}</h1>
    <p>By: {{routine.user.username}}</p>
    <div class="bg-light d-inline-block p-2">
      <span class="badge bg-dark ms-1" v-for="category in routine.categories" :key="category.id">{{category.name}}</span>
    </div>
  </div>

  <WorkoutCard v-for="userWorkout in routine.user_workouts" :key="userWorkout.id"
               :workout="userWorkout" 
               :isOwner="isOwner" />

  <CreateWorkoutWindow v-if="isOwner" 
                        :routineId="routine.id"
                        @createWorkoutEmit="fetchRoutineData" />

</template>

<script>
import axios from 'axios'
import WorkoutCard from '@/components/WorkoutCard'
import CreateWorkoutWindow from '@/components/CreateWorkoutWindow'
import jwt_decode from "jwt-decode";

export default {
  name: 'Routine',
  components: {
    WorkoutCard, CreateWorkoutWindow
  },
  data () {
      return {
        routine: {
          id: 0,
          user: {
            username: "",
            id: 1
          },
          user_workouts: []
        },
        isOwner: false
      }
  },
  mounted() {
      this.fetchRoutineData()
      this.isRoutineOwner()
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
    isRoutineOwner() {
      if (this.$store.state.isAuthenticated) {
        let authenticatedUser = jwt_decode(this.$store.state.accessToken)
        this.isOwner = authenticatedUser.user_id === this.routine.user.id
      }
    }
  }
}
</script>