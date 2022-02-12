import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    accessToken: '',
    refreshToken: ''
  },
  mutations: {
    authenticated(state, access, refresh) {
      state.accessToken = access
      localStorage.setItem("accessToken", access)
      state.refreshToken = refresh
      localStorage.setItem("refreshToken", refresh)
      state.isAuthenticated = true
    },
    deauthenticated(state) {
      state.accessToken = ""
      localStorage.removeItem('accessToken');
      state.refreshToken = "refreshToken"
      state.isAuthenticated = false
    },
    initializeStore(state) {
      if (localStorage.getItem('accessToken')) {
        state.accessToken = localStorage.getItem('accessToken')
        state.isAuthenticated = true
      } else {
        state.accessToken = ''
        state.isAuthenticated = false
      }

      if (localStorage.getItem('refreshToken')) {
        state.refreshToken = localStorage.getItem('refreshToken')
      } else {
        state.refreshToken = ''
      }
    },
  },
  actions: {

  },
  modules: {
  }
})
