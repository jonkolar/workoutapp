import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import jwt_decode from "jwt-decode"
import { Tooltip } from "bootstrap"

axios.defaults.baseURL = 'http://localhost:8000';

axios.defaults.withCredentials = true;

axios.interceptors.response.use((response, error) => {
    if (error) {
        console.log("Error: " + error)
        return error
    }
    return response
})

// Retry requests on failure
const retryWrapper = (axios) => {
    const maxTries = 5
    let tryCount = 0

    axios.interceptors.response.use((response) => { return response }, (error) => {
        if (tryCount < 10) {
            tryCount++
            return new Promise((resolve) => {
                resolve(axios(error.config))
            })
        } 
        return Promise.reject(error)
    })
}

axios.interceptors.request.use(async (config) => {
    if (store.getters['getIsAuthenticated']) {
        let tokens = store.getters['getTokens']
        let decodedAccessToken = jwt_decode(tokens['accessToken'])
        let decodedRefreshToken = jwt_decode(tokens['refreshToken'])

        let accessTokenExpiryTime = new Date(decodedAccessToken.exp * 1000)
        let refreshTokenExpiryTime = new Date(decodedRefreshToken.exp * 1000)

        if (accessTokenExpiryTime <= Date.now() && refreshTokenExpiryTime > Date.now()){ // Access Token is expired AND Refresh Token is NOT expired
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

const app = createApp(App)

retryWrapper(axios)

app.directive("tooltip", {
    mounted(el, binding) {
        new Tooltip(el)
    }
})

app.use(store).use(router).mount('#app')
