import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000', // FastAPI backend
})

// Add an interceptor to automatically attach JWT token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default api
