import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

interface HealthStatus {
  status: string
}

function App() {
  const [status, setStatus] = useState<string>('checking...')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await axios.get<HealthStatus>('/api/health')
        setStatus(response.data.status)
        setError(null)
      } catch (err) {
        setError('Failed to connect to API')
        setStatus('offline')
      } finally {
        setLoading(false)
      }
    }

    checkHealth()
  }, [])

  return (
    <div className="container">
      <header>
        <h1>Advanced Test Project</h1>
        <p>Full-stack application with comprehensive testing</p>
      </header>

      <main>
        <div className="status-card">
          <h2>API Status</h2>
          {loading ? (
            <p>Checking API connection...</p>
          ) : (
            <>
              <p className={`status ${status}`}>Status: {status}</p>
              {error && <p className="error">{error}</p>}
            </>
          )}
        </div>

        <section className="info">
          <h2>Project Information</h2>
          <ul>
            <li>Backend: FastAPI with REST API, gRPC, WebSocket</li>
            <li>Testing: Complete test pyramid with pytest</li>
            <li>Database: PostgreSQL with SQLAlchemy ORM</li>
            <li>Cache: Redis</li>
            <li>DevOps: Docker, GitHub Actions, Allure</li>
          </ul>
        </section>

        <section className="links">
          <h2>Resources</h2>
          <a href="http://localhost:8000/docs" target="_blank">
            API Documentation (Swagger)
          </a>
          <a href="https://github.com/DronovNA/advanced-test-project" target="_blank">
            GitHub Repository
          </a>
        </section>
      </main>

      <footer>
        <p>&copy; 2025 Advanced Test Project. All rights reserved.</p>
      </footer>
    </div>
  )
}

export default App
