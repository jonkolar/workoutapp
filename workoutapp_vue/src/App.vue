<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/explore">Explore</router-link> |
    <template v-if="$store.state.isAuthenticated">
    <router-link to="/dashboard/routines">Routines</router-link> |
      <button @click="logout">Logout</button>
    </template>
    <template v-else>
      <router-link to="/sign-up">Register</router-link> |
      <router-link to="/login">Login</router-link>
    </template>
  </div>
  <!-- LOADING ICON --> 
  <div v-if="isLoading" class="spinner-border" role="status"></div>
  <!-- END LOADING ICON -->
  <router-view />
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import axios from 'axios'
import jwt_decode from "jwt-decode";

export default {
  data () {
    return {
      isLoading: false,
      showMobileMenu: false,
      isModalOpen: false
    }
  },
  mixins: [],
  created(){
      this.$store.commit('initializeStore')

      if (this.$store.state.isAuthenticated) {
        const accessToken = this.$store.state.accessToken
        const refreshToken = this.$store.state.refreshToken

        let decodedRefreshToken = jwt_decode(refreshToken)
        let refreshTokenExpiryTime = new Date(decodedRefreshToken.exp * 1000)

        if (refreshTokenExpiryTime > Date.now()){
          axios.defaults.headers.common['Authorization'] = "Bearer " + accessToken
        } else {
          this.logout()
        }
      }
  },
  methods: {
    toggleIsLoading(bool) {
      this.isLoading = bool
    },
    toggleIsModalOpen(bool) {
      this.IsModalOpen = bool
      if (bool) { $('body').css('overflow', 'hidden'); } else { $('body').css('overflow', 'auto'); }
    },
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

.pointerButton:hover {
  cursor: pointer;
}

.modal-open {
  overflow: hidden;
}
</style>
