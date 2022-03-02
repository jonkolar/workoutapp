<template>

  <div class="container-fluid d-flex justify-content-center">
    <WorkoutCard 
      v-for="workout in userWorkouts"
      v-bind:key="workout.id"
      v-bind:workout="workout" />
  </div>

</template>

<script>
import axios from 'axios'
import WorkoutCard from '@/components/WorkoutCard'

export default {
  name: 'MyRoutines',
  components: {
    WorkoutCard
  },
  data () {
      return {
        userWorkouts: [],
      }
  },
  methods: {
      
  },
  mounted() {
      axios.get(`/api/routines/user/all`)
        .then((response) => {
          for(let i = 0; i < response.data.length; i++){
            //this.userWorkouts.push(response.data[i])
          }
        })
  }
}
</script>