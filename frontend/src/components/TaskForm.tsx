import { useState } from 'react'
import { CreateTaskRequest } from '../types'

interface Props {
  onSubmit: (task: CreateTaskRequest) => void
}

export const TaskForm = ({ onSubmit }: Props) => {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (title.trim()) {
      onSubmit({ title, description: description || undefined, completed: false })
      setTitle('')
      setDescription('')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="task-form">
      <input
        type="text"
        placeholder="Task title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="task-input"
        id="task-title"
        required
      />
      <textarea
        placeholder="Task description (optional)"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        className="task-textarea"
        id="task-description"
      />
      <button type="submit" className="submit-btn" id="create-task-btn">
        Add Task
      </button>
    </form>
  )
}