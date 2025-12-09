# Настройка Окружения Разработки

## Предварительные требования

- Python 3.11 или выше
- Node.js 18 или выше
- Docker & Docker Compose
- Git
- PostgreSQL 15 (или использовать Docker)
- Redis 7 (или использовать Docker)

## Быстрый старт с Docker

### 1. Клонирование репозитория

```bash
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project
```

### 2. Запуск сервисов

```bash
docker-compose up --build
```

Это будет:
- Собрать Docker образ бэкенда
- Запустить PostgreSQL на порту 5432
- Запустить Redis на порту 6379
- Запустить FastAPI бэкенд на порту 8000

### 3. Проверка установки

```bash
# Проверка здоровья API
curl http://localhost:8000/health

# Просмотр документации API
open http://localhost:8000/docs
```

## Локальная разработка

### Настройка Бэкенда

```bash
cd backend

# Создание виртуального окружения
python3.11 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Создание .env файла
cp .env.example .env

# Обновить .env с локальными credentials БД
# DATABASE_URL=postgresql://user:password@localhost:5432/testdb
# REDIS_URL=redis://localhost:6379/0
```

### Запуск Приложения

```bash
uvicorn app.main:app --reload
```

Бэкенд будет доступен на `http://localhost:8000`
Документация API на `http://localhost:8000/docs`

### Запуск Тестов

```bash
# Все тесты
pytest -v

# Только unit тесты
pytest tests/unit/ -v

# С покрытием
pytest --cov=app --cov-report=html

# Конкретные маркеры
pytest -m smoke -v
pytest -m regression -v

# Параллельное выполнение (быстрее)
pytest -n auto
```

### Управление Базой Данных

```bash
# Проверка подключения
psql -U testuser -h localhost -d testdb

# Просмотр таблиц
\dt

# Пересоздание БД (используйте осторожно)
DROP DATABASE testdb;
CREATE DATABASE testdb;
```

## Конфигурация IDE

### VS Code

Создайте `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["backend/tests"]
}
```

### PyCharm

1. Конфигурация интерпретатора: Settings → Project → Python Interpreter → Add Local
2. Выберите `backend/venv/bin/python`
3. Отметьте `backend/tests` как Test Sources Root
4. Включите pytest: Settings → Tools → Python Integrated Tools → pytest

## Переменные Окружения

Создайте `backend/.env`:

```bash
# База Данных
DATABASE_URL=postgresql://testuser:testpass@localhost:5432/testdb

# Redis
REDIS_URL=redis://localhost:6379/0

# Приложение
SECRET_KEY=your-secret-key-here
DEBUG=true
ENVIRONMENT=development
```

## Типичные Проблемы

### Ошибка Подключения к БД

```bash
# Проверьте, работает ли PostgreSQL
docker-compose ps

# Перезапустите сервисы
docker-compose restart postgres

# Просмотрите логи
docker-compose logs postgres
```

### Порт уже занят

```bash
# Найдите процесс на порту 8000
lsof -i :8000

# Прекратите процесс
kill -9 <PID>
```

### Ошибки импорта в тестах

```bash
# Убедитесь, что backend в Python path
export PYTHONPATH="${PYTHONPATH}:${PWD}/backend"

# Или запустите из backend директории
cd backend
pytest tests/
```

## Следующие Шаги

- Прочитайте [TESTING.md](TESTING.md) для стратегии тестирования
- Проверьте [API.md](API.md) для документации endpoints
- Изучите код в `backend/app/` для паттернов архитектуры
- Запустите тесты: `pytest -v`
