<template>
  <div>
    <form class="w-50 p-3 mx-auto" @submit.prevent="submitRegistration">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" v-model="username" class="form-control" id="username">
      </div>
      <div class="mb-3">
        <label for="password1" class="form-label">Password:</label>
        <input type="password" v-model="password1" class="form-control" id="password1">
      </div>
      <div class="mb-3">
        <label for="password2" class="form-label">Confirm Password:</label>
        <input type="password" v-model="password2" class="form-control" id="password2">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUp',
  components: {
    
  },
  data () {
      return {
        username: "",
        password1: "",
        password2: "",
      }
  },
  methods: {
      submitRegistration() {

        // Form Validation
        console.log(this.username + this.password1 + this.password2)
        axios.post(`/api/v1/users/`, {
          username: this.username,
          password: this.password1
        })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
      }
  }
}
</script>