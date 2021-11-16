import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  setInterval(() => {
    // console.log('test')
    getCounter()
  }, 2000)

  const getCounter = () => {
    fetch('http://localhost:8081/api/get?key=test')
      .then((res) => res.json())
      .then((data) => setCount(data.value))
      .catch(e => console.log(e))
  }
  return (
    <div className="App">
      <div style={{ fontSize: '600px' }}>{count}</div>
    </div>
  )
}

export default App
