<template>

  <div class="container-fluid d-flex justify-content-center">
    <RoutineCard 
      v-for="routine in userRoutines"
      v-bind:key="routine.id"
      v-bind:routine="routine" />
  </div>

</template>

<script>
import axios from 'axios'
import RoutineCard from '@/components/RoutineCard'

export default {
  name: 'MyRoutines',
  components: {
    RoutineCard
  },
  data () {
      return {
        userRoutines: [],
      }
  },
  methods: {
      
  },
  mounted() {
      axios.get(`/api/routines/user/all`)
        .then((response) => {
          for(let i = 0; i < response.data.length; i++){
            this.userRoutines.push(response.data[i])
          }
        })
  }
}
</script>