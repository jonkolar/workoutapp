<template>
  <div>
    <h1>{{routine.name}}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Routine',
  components: {
    
  },
  data () {
      return {
        routine: {},
        userRoutineWorkouts: []
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
          console.log(this.routine)

      this.$root.toggleIsLoading(false)
    }
  },
}
</script>