import { Link, useNavigate } from 'react-router-dom'
import { useEffect, useState, useRef } from 'react'
import './Navbar.css'
import logo from '../assets/jira.png'

export default function Navbar() {
  const [username, setUsername] = useState('')
  const [menuOpen, setMenuOpen] = useState(false)
  const [dropdownOpen, setDropdownOpen] = useState(false)
  const navigate = useNavigate()



  const handleLogout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    navigate('/login')
  }

  return (
    <header className="navbar">
      <div className="navbar__left">
        
        <h1>Dashboard</h1>
      </div>

      <nav className={`navbar__right ${menuOpen ? 'open' : ''}`}>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/projects">Projects</Link>
        <div className="dropdown">
          <button onClick={() => setDropdownOpen((prev) => !prev)}>
            {username || 'User'} ▾
          </button>
          {dropdownOpen && (
            <div className="dropdown-content">
              <button onClick={handleLogout}>Logout</button>
            </div>
          )}
        </div>
      </nav>

      <button className="navbar__toggle" onClick={() => setMenuOpen(!menuOpen)}>
        ☰
      </button>
    </header>
  )
}
