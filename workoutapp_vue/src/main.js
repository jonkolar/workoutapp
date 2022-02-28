import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import jwt_decode from "jwt-decode"

axios.defaults.baseURL = 'http://localhost:8000';

axios.defaults.withCredentials = true;

axios.interceptors.request.use(async (config) => {
    if (store.getters['getIsAuthenticated']) {
        let tokens = store.getters['getTokens']
        let decodedAccessToken = jwt_decode(tokens['accessToken'])
        let decodedRefreshToken = jwt_decode(tokens['refreshToken'])

        let accessTokenExpiryTime = new Date(decodedAccessToken.exp * 1000)
        let refreshTokenExpiryTime = new Date(decodedRefreshToken.exp * 1000)

        if (accessTokenExpiryTime <= Date.now() && refreshTokenExpiryTime > Date.now()){ // Access Token is expired AND Refresh Token is NOT expired
            console.log("REQUESTING NEW ACCESS TOKEN")
            const newAccessToken = await retrieveNewAccessToken(tokens['refreshToken'])

            config.headers['Authorization'] = "Bearer " + newAccessToken
        }
    }

    return config
})

async function retrieveNewAccessToken(refreshToken) {
    const tokenAPI = axios.create({
        baseURL: axios.defaults.baseURL,
        timeout: 1000,
    })

    const response = await tokenAPI.post('/api/token/refresh/', {
        refresh: refreshToken
    })

    store.commit('authenticated', {access: response.data['access'], refresh: refreshToken})
            axios.defaults.headers.common["Authorization"] = "Bearer " + response.data['access']
    
    return response.data['access']
}

createApp(App).use(store).use(router).mount('#app')
