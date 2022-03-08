import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Routine from '../views/Routine.vue'
import DashboardRoutines from '../views/DashboardRoutines.vue'
import store from '@/store'

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
    path: '/dashboard/routines',
    name: 'DashboardRoutines',
    component: DashboardRoutines,
    beforeEnter: (to, from, next) => { // Add Authenticated Guard to more Routes
      if(!store.getters['getIsAuthenticated']) {
        return next({
          name: 'Login'
        })
      }
      next()
    }
  },
  {
  path: '/routine/:id',
    name: 'Routine',
    component: Routine
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
