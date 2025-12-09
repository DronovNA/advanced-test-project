# Документация API

## Базовый URL

```
http://localhost:8000/api/v1
```

## Проверка Здоровья

### GET /health

Проверка статуса здоровья API.

```bash
curl http://localhost:8000/health
```

**Ответ**:
```json
{
    "status": "ok"
}
```

## Пользователи

### POST /users/

Создание нового пользователя.

**Запрос**:
```json
{
    "email": "user@example.com",
    "username": "username",
    "password": "password123"
}
```

**Ответ**: `201 Created`
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

Получить пользователя по ID.

**Ответ**: `200 OK`
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

Список пользователей с пагинацией.

**Параметры Запроса**:
- `skip` (опционально): Количество записей пропустить (по умолчанию: 0)
- `limit` (опционально): Количество записей вернуть (по умолчанию: 10)

**Ответ**: `200 OK`
```json
[
    {
        "id": 1,
        "email": "user1@example.com",
        "username": "user1",
        "is_active": true,
        "created_at": "2025-12-09T12:00:00"
    }
]
```

## Задачи

### POST /tasks/

Создание новой задачи.

**Параметры Запроса**:
- `owner_id` (обязательно): ID владельца задачи

**Запрос**:
```json
{
    "title": "Моя Задача",
    "description": "Описание задачи",
    "completed": false
}
```

**Ответ**: `201 Created`
```json
{
    "id": 1,
    "title": "Моя Задача",
    "description": "Описание задачи",
    "owner_id": 1,
    "completed": false,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:00:00"
}
```

### GET /tasks/{task_id}

Получить задачу по ID.

**Ответ**: `200 OK`
```json
{
    "id": 1,
    "title": "Моя Задача",
    "description": "Описание задачи",
    "owner_id": 1,
    "completed": false,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:00:00"
}
```

### GET /tasks/

Список задач пользователя с пагинацией.

**Параметры Запроса**:
- `owner_id` (обязательно): ID владельца
- `skip` (опционально): Количество пропустить (по умолчанию: 0)
- `limit` (опционально): Количество вернуть (по умолчанию: 10)

**Ответ**: `200 OK`
```json
[
    {
        "id": 1,
        "title": "Задача 1",
        "description": "Описание",
        "owner_id": 1,
        "completed": false,
        "created_at": "2025-12-09T12:00:00",
        "updated_at": "2025-12-09T12:00:00"
    }
]
```

### PUT /tasks/{task_id}

Обновление задачи.

**Запрос**:
```json
{
    "title": "Обновленная Задача",
    "description": "Обновленное описание",
    "completed": true
}
```

**Ответ**: `200 OK`
```json
{
    "id": 1,
    "title": "Обновленная Задача",
    "description": "Обновленное описание",
    "owner_id": 1,
    "completed": true,
    "created_at": "2025-12-09T12:00:00",
    "updated_at": "2025-12-09T12:05:00"
}
```

## Ответы об Ошибках

### 400 Неверный Запрос
```json
{
    "detail": "Email уже зарегистрирован"
}
```

### 404 Не Найдено
```json
{
    "detail": "Пользователь не найден"
}
```
