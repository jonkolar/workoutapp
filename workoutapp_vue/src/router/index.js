import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import MyWorkouts from '../views/MyWorkouts.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/my-workouts',
    name: 'MyWorkouts',
    component: MyWorkouts
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
