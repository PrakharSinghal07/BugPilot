import { useState } from 'react'
import '../styles/Auth.css'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../Context/AuthContext'
export default function Login() {
  const {login} = useAuth()
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  })
  const navigate = useNavigate()
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const formDataForRequest = new URLSearchParams()
    formDataForRequest.append("username", formData.username)
    formDataForRequest.append("password", formData.password)

    try {
      const response = await axios.post('http://localhost:8000/users/login', formDataForRequest, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',  // Ensure correct content type
        }
      })

      // Debugging: Check if token is received
      login(response.data.access_token)
      // localStorage.setItem('token', response.data.access_token)
      navigate('/dashboard')
      console.log(response);
    } catch (error) {
      console.log('Login failed:', error) // Log the error in case of a failed request
    }
  }

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={handleSubmit}>
        <h2>Login</h2>
        <input
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
        />
        <button type="submit">Login</button>
        <a href='/register' className='sign-in-text'>or Sign In</a>
      </form>
    </div>
  )
}
