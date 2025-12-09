export interface User {
  id: number
  email: string
  username: string
  is_active: boolean
  created_at: string
}

export interface Task {
  id: number
  title: string
  description?: string
  owner_id: number
  completed: boolean
  created_at: string
  updated_at?: string
}

export interface CreateUserRequest {
  email: string
  username: string
  password: string
}

export interface CreateTaskRequest {
  title: string
  description?: string
  completed?: boolean
}

export interface UpdateTaskRequest {
  title: string
  description?: string
  completed: boolean
}