<template>
  <div id="nav">
      <router-link to="/">Home</router-link> |
    <template v-if="$store.state.isAuthenticated">
      <router-link to="/my-workouts">MyWorkouts</router-link> |
      <button @click="logout">Logout</button>
    </template>
    <template v-else>
      <router-link to="/sign-up">Register</router-link> |
      <router-link to="/login">Login</router-link>
    </template>
  </div>
  <router-view/>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.accessToken

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    logout() {
        axios.defaults.headers.common["Authorization"] = ""

        this.$store.commit('deauthenticated')

        this.$router.push('/')
        },
  }
}
</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
