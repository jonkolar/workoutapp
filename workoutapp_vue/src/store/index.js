import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    accessToken: '',
    refreshToken: ''
  },
  mutations: {
    authenticated(state, access, refresh){
      state.accessToken = access
      state.refreshToken = refresh
      state.isAuthenticated = true
    },
    deauthenticated(state){
      state.accessToken = "",
      state.refreshToken = "",
      state.isAuthenticated = false
    }
  },
  actions: {

  },
  modules: {
  }
})
