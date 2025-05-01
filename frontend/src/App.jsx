import { useEffect, useState } from "react";

function App() {
  const [ping, setPing] = useState("")
  useEffect(() => {
    const callBackend = async () => {
      const response = await fetch('http://127.0.0.1:8000/ping')
      const result = await response.json()
      setPing(result.message)
    }
    callBackend()
  }, [])
  return (
    <div>
      <h1>Mini Jira Bug Tracker</h1>
      <p>Frontend is working!</p>
      <p>Backend says {ping}!</p>
    </div>
  );
}

export default App;
