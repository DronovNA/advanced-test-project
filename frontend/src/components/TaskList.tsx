import { Task } from '../types'

interface Props {
  tasks: Task[]
  onToggle: (id: number) => void
  onDelete: (id: number) => void
}

export const TaskList = ({ tasks, onToggle, onDelete }: Props) => {
  return (
    <div className="task-list">
      {tasks.length === 0 ? (
        <p className="no-tasks">No tasks yet. Create your first task!</p>
      ) : (
        tasks.map(task => (
          <div key={task.id} className={`task-item ${task.completed ? 'completed' : ''}`}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => onToggle(task.id)}
              className="task-checkbox"
            />
            <div className="task-content">
              <h3 className="task-title">{task.title}</h3>
              {task.description && <p className="task-description">{task.description}</p>}
            </div>
            <button onClick={() => onDelete(task.id)} className="delete-btn">
              Delete
            </button>
          </div>
        ))
      )}
    </div>
  )
}