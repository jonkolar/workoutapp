<template>
  <div class="container-fluid d-flex justify-content-center flex-wrap">
    <RoutineCard 
      v-for="routine in userRoutines"
      v-bind:key="routine.id"
      v-bind:routine="routine" />
  </div>

  <div>
    <i class="bi bi-plus-square-fill bi-3x" style="font-size: 40px" @click="toggleCreateRoutineWindow(true)"></i>
  </div>
  
  <CreateRoutineWindow v-if="showCreateRoutineWindow"
    @toggleWindow="toggleCreateRoutineWindow" 
    @fetchUserRoutines="fetchUserRoutines" />


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
        showCreateRoutineWindow: false,
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
    toggleCreateRoutineWindow(bool) {
        this.showCreateRoutineWindow = bool
    }
  }
}
</script>

<style scoped>

</style>