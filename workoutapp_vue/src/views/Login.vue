<template>
  <div>
    <form class="w-50 p-3 mx-auto" @submit.prevent="submitLogin">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" v-model="username" class="form-control" id="username" required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" v-model="password" class="form-control" id="password" required>
      </div>
      <div class="alert alert-danger" role="alert" v-for="error in errors">
        {{error}}
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  components: {
    
  },
  data () {
      return {
        username: "",
        password: "",
        errors: [],
      }
  },
  methods: {
      submitLogin() {
        this.errors = []

        let data = {
            username: this.username,
            password: this.password,
        }

        axios.post('/api/token/', data)
        .then((response) => {
          console.log(response)

          axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
          this.$store.commit('authenticated', response.data.access, response.data.refresh)
        })
      },
  }
}
</script>