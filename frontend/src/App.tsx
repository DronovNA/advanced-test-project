import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'
import { Task, CreateTaskRequest } from './types'
import { TaskList } from './components/TaskList'
import { TaskForm } from './components/TaskForm'

function App() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const mockUserId = 1

  useEffect(() => {
    loadTasks()
  }, [])

  const loadTasks = async () => {
    try {
      const response = await axios.get(`/api/v1/tasks/?owner_id=${mockUserId}`)
      setTasks(response.data)
      setError(null)
    } catch (err) {
      setError('Failed to load tasks')
    } finally {
      setLoading(false)
    }
  }

  const createTask = async (taskData: CreateTaskRequest) => {
    try {
      const response = await axios.post(`/api/v1/tasks/?owner_id=${mockUserId}`, taskData)
      setTasks([...tasks, response.data])
    } catch (err) {
      setError('Failed to create task')
    }
  }

  const toggleTask = async (id: number) => {
    const task = tasks.find(t => t.id === id)
    if (!task) return

    try {
      const response = await axios.put(`/api/v1/tasks/${id}`, {
        title: task.title,
        description: task.description,
        completed: !task.completed
      })
      setTasks(tasks.map(t => t.id === id ? response.data : t))
    } catch (err) {
      setError('Failed to update task')
    }
  }

  const deleteTask = async (id: number) => {
    try {
      await axios.delete(`/api/v1/tasks/${id}`)
      setTasks(tasks.filter(t => t.id !== id))
    } catch (err) {
      setError('Failed to delete task')
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Task Manager</h1>
        <p>Advanced Test Project</p>
      </header>

      <main className="app-main">
        {error && <div className="error-message">{error}</div>}
        
        <TaskForm onSubmit={createTask} />
        
        {loading ? (
          <p>Loading tasks...</p>
        ) : (
          <TaskList tasks={tasks} onToggle={toggleTask} onDelete={deleteTask} />
        )}
      </main>
    </div>
  )
}

export default App