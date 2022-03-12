<template>
  <div>
    <h1>{{routine.name}}</h1>
    <p>By: {{routine.user.username}}</p>
  </div>

  <WorkoutCard v-for="userWorkout in routine.user_workouts" :key="userWorkout.id"
               :workout="userWorkout" />


</template>

<script>
import axios from 'axios'
import WorkoutCard from '@/components/WorkoutCard'

export default {
  name: 'Routine',
  components: {
    WorkoutCard
  },
  data () {
      return {
        routine: {
          user: {
            username: ""
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
    }
  },
}
</script>