import React, { createContext, useContext, useEffect, useState } from "react";
const AuthContext = createContext();
export function AuthProvider({ children }) {
  const [token, setToken] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(useState(!!localStorage.getItem("token")))
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken){
      setToken(storedToken)
      setIsAuthenticated(true)
    }
  }, []);


  const login = (loginToken) => {
    localStorage.setItem("token", loginToken);
    setToken(loginToken);
    setIsAuthenticated(true)
  };

  const logout = () => {
    localStorage.removeItem('token')
    setToken(null)
    setIsAuthenticated(false)
  }

  return <AuthContext.Provider value={{token, login, logout, isAuthenticated}}>{children}</AuthContext.Provider>;
}


export const useAuth = () => useContext(AuthContext)