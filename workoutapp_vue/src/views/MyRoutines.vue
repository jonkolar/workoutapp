<template>
  <div class="container-fluid d-flex justify-content-center flex-wrap">
    <RoutineCard 
      v-for="routine in userRoutines"
      v-bind:key="routine.id"
      v-bind:routine="routine" />
  </div>

  <CreateRoutineWindow
    @createRoutineEmit="fetchUserRoutines" />


</template>

<script>
import axios from 'axios'
import RoutineCard from '@/components/RoutineCard'
import CreateRoutineWindow from '@/components/CreateRoutineWindow'

export default {
  name: 'MyRoutines',
  components: {
    RoutineCard,
    CreateRoutineWindow
  },
  data () {
      return {
        userRoutines: [],
      }
  },
  mounted() {
    this.fetchUserRoutines()
  },
  methods: {
    async fetchUserRoutines() {
        this.$root.toggleIsLoading(true)
        this.userRoutines = []

          await axios.get(`/api/dashboard/routines/all`)
          .then((response) => {
            for(let i = 0; i < response.data.length; i++){
              this.userRoutines.push(response.data[i])
            }
          })

        this.$root.toggleIsLoading(false)
    },
  }
}
</script>

<style scoped>

</style>