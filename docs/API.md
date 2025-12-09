# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Health Check

### GET /health

Check API health status.

```bash
curl http://localhost:8000/health
```

**Response**:
```json
{
    "status": "ok"
}
```

## Users

### POST /users/

Create a new user.

**Request**:
```json
{
    "email": "user@example.com",
    "username": "username",
    "password": "password123"
}
```

**Response**: `201 Created`
```json
{
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "is_active": true,
    "created_at": "2025-12-09T12:00:00"
}
```

### GET /users/{user_id}

Get user by ID.

**Response**: `200 OK`
```json
{
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "is_active": true,
    "created_at": "2025-12-09T12:00:00"
}
```

### GET /users/

List users with pagination.

**Query Parameters**:
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Number of records to return (default: 10)

**Response**: `200 OK`
```json
[
    {
        "id": 1,
        "email": "user1@example.com",
        "username": "user1",
        "is_active": true,
        "created_at": "2025-12-09T12:00:00"
    },
    {
        "id": 2,
        "email": "user2@example.com",
        "username": "user2",
        "is_active": true,
        "created_at": "2025-12-09T12:01:00"
    }
]
```

## Tasks

### POST /tasks/

Create a new task.

**Query Parameters**:
- `owner_id` (required): ID of the task owner

**Request**:
```json
{
    "title": "My Task",
    "description": "Task description",
    "completed": false
}
```

**Response**: `201 Created`
```json
{
    "id": 1,
    "title": "My Task",
    "description": "Task description",
    "owner_id": 1,
    "completed": false,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:00:00"
}
```

### GET /tasks/{task_id}

Get task by ID.

**Response**: `200 OK`
```json
{
    "id": 1,
    "title": "My Task",
    "description": "Task description",
    "owner_id": 1,
    "completed": false,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:00:00"
}
```

### GET /tasks/

List user's tasks with pagination.

**Query Parameters**:
- `owner_id` (required): ID of the task owner
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Number of records to return (default: 10)

**Response**: `200 OK`
```json
[
    {
        "id": 1,
        "title": "Task 1",
        "description": "Description",
        "owner_id": 1,
        "completed": false,
        "created_at": "2025-12-09T12:00:00",
        "updated_at": "2025-12-09T12:00:00"
    }
]
```

### PUT /tasks/{task_id}

Update a task.

**Request**:
```json
{
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
}
```

**Response**: `200 OK`
```json
{
    "id": 1,
    "title": "Updated Task",
    "description": "Updated description",
    "owner_id": 1,
    "completed": true,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:05:00"
}
```

## Error Responses

### 400 Bad Request
```json
{
    "detail": "Email already registered"
}
```

### 404 Not Found
```json
{
    "detail": "User not found"
}
```

## Testing with curl

```bash
# Create user
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"testuser","password":"pass123"}'

# Get user
curl http://localhost:8000/api/v1/users/1

# Create task
curl -X POST http://localhost:8000/api/v1/tasks/?owner_id=1 \
  -H "Content-Type: application/json" \
  -d '{"title":"My Task","description":"Task desc","completed":false}'

# Update task
curl -X PUT http://localhost:8000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated","description":"New desc","completed":true}'
```

## API Documentation UI

Swagger UI is available at: `http://localhost:8000/docs`
ReDoc is available at: `http://localhost:8000/redoc`
