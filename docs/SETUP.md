# Development Environment Setup

## Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- Docker & Docker Compose
- Git
- PostgreSQL 15 (or use Docker)
- Redis 7 (or use Docker)

## Quick Start with Docker

### 1. Clone the repository

```bash
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project
```

### 2. Start services

```bash
docker-compose up --build
```

This will:
- Build the backend Docker image
- Start PostgreSQL on port 5432
- Start Redis on port 6379
- Start FastAPI backend on port 8000

### 3. Verify installation

```bash
# Check API health
curl http://localhost:8000/health

# View API documentation
open http://localhost:8000/docs
```

## Local Development Setup

### Backend Setup

```bash
cd backend

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Update .env with local database credentials
# DATABASE_URL=postgresql://user:password@localhost:5432/testdb
# REDIS_URL=redis://localhost:6379/0
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Backend will be available at `http://localhost:8000`
API docs at `http://localhost:8000/docs`

### Run Tests

```bash
# All tests
pytest -v

# Unit tests only
pytest tests/unit/ -v

# With coverage
pytest --cov=app --cov-report=html

# Specific markers
pytest -m smoke -v
pytest -m regression -v

# Parallel execution (faster)
pytest -n auto
```

### Database Management

```bash
# Check database connection
psql -U testuser -h localhost -d testdb

# View tables
\dt

# Drop and recreate (use with caution)
DROP DATABASE testdb;
CREATE DATABASE testdb;
```

## Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## IDE Configuration

### VS Code

Create `.vscode/settings.json`:

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

1. Configure interpreter: Settings → Project → Python Interpreter → Add Local
2. Select `backend/venv/bin/python`
3. Mark `backend/tests` as Test Sources Root
4. Enable pytest: Settings → Tools → Python Integrated Tools → pytest

## Environment Variables

Create `backend/.env`:

```bash
# Database
DATABASE_URL=postgresql://testuser:testpass@localhost:5432/testdb

# Redis
REDIS_URL=redis://localhost:6379/0

# Application
SECRET_KEY=your-secret-key-here
DEBUG=true
ENVIRONMENT=development
```

## Common Issues

### Database Connection Error

```bash
# Check PostgreSQL is running
docker-compose ps

# Restart services
docker-compose restart postgres

# Check logs
docker-compose logs postgres
```

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Import Errors in Tests

```bash
# Ensure backend is in Python path
export PYTHONPATH="${PYTHONPATH}:${PWD}/backend"

# Or run from backend directory
cd backend
pytest tests/
```

## Next Steps

- Read [TESTING.md](TESTING.md) for testing strategy
- Check [API.md](API.md) for endpoint documentation
- Review code in `backend/app/` for architecture patterns
- Run tests: `pytest -v`
