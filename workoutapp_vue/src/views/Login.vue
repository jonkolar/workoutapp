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
      getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
            }
        }
        console.log(cookieValue)
        return cookieValue;
     },
      submitLogin() {
        this.errors = []

        let data = {
            username: this.username,
            password: this.password,
            'X-CSRFToken': this.getCookie('csrftoken')
        }

        axios.post('/api/user/login/', data)
        .then((response) => {
          console.log(response)
        })
      },
  }
}
</script>