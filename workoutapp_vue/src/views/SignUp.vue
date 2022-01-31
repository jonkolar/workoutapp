<template>
  <div>
    <form class="w-50 p-3 mx-auto" @submit.prevent="submitRegistration">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" v-model="username" class="form-control" id="username" required>
      </div>
      <div class="mb-3">
        <label for="password1" class="form-label">Password:</label>
        <input type="password" v-model="password1" class="form-control" id="password1" required>
      </div>
      <div class="mb-3">
        <label for="password2" class="form-label">Confirm Password:</label>
        <input type="password" v-model="password2" class="form-control" id="password2" required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="email" v-model="email" class="form-control" id="email" required>
      </div>
      <div class="alert alert-danger" role="alert" v-for="error in errors">
        {{error}}
      </div>
      <div class="alert alert-success" role="alert" id="register-success-alert" style="display: none">
        You have succesfully registered!
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
        email: "",
        errors: [],
      }
  },
  methods: {
      submitRegistration() {

        $('#register-success-alert').hide()
        this.errors = []

        if (this.password1 !== this.password2){
          this.errors.push("Password's do not match!")
        }

        if (this.errors.length == 0){
          axios.post(`/api/v1/users/`, {
            username: this.username,
            password: this.password1,
            email: this.email
          })
          .then((response) => {
            console.log(response)

            $('#register-success-alert').show()
            this.username = ""
            this.password1 = ""
            this.password2 = ""
            this.email = ""
          })
          .catch((error) => {
            for (const property in error.response.data) {
              this.errors.push(`${error.response.data[property]}`)
            }
          })
        }
      }
  }
}
</script>