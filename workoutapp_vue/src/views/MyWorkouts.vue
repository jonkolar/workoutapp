<template>
  <div>
    <h1>HEY!</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyWorkouts',
  components: {
    
  },
  data () {
      
  },
  methods: {
      
  },
  mounted() {
      console.log(axios.defaults.headers.common['Authorization'])
      axios.get('/api/workout/spirks/1/')
        .then((response) => {

        })
  }
}
</script>