# Advanced Test Project

[![Tests](https://github.com/DronovNA/advanced-test-project/workflows/Test%20Suite/badge.svg)](https://github.com/DronovNA/advanced-test-project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)

**A comprehensive full-stack web application with production-grade test suite demonstrating advanced testing practices, design patterns, and DevOps workflows.**

## 📋 Overview

This project showcases:
- **Backend**: FastAPI with REST API, gRPC, WebSocket support
- **Frontend**: React with TypeScript components
- **Database**: PostgreSQL with SQLAlchemy ORM + Redis caching
- **Testing**: Complete testing pyramid (Unit → Integration → E2E)
- **CI/CD**: GitHub Actions with Allure reports
- **Containerization**: Docker & Docker Compose

### 🎯 Target Audience
- QA Engineers seeking to demonstrate testing expertise
- Freelancers building portfolio projects
- Teams evaluating test automation frameworks

---

## 📁 Project Structure

```
advanced-test-project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── rest/
│   │   │   ├── grpc/
│   │   │   └── websocket/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database/
│   │   └── config.py
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   ├── e2e/
│   │   ├── fixtures/
│   │   └── conftest.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── services/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .github/workflows/
│   ├── tests.yml
│   └── deploy.yml
├── docs/
│   ├── API.md
│   ├── TESTING.md (RU/EN)
│   └── SETUP.md (RU/EN)
└── pytest.ini
```

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- Git

### Setup & Run

```bash
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project

docker-compose up --build
```

Backend: `http://localhost:8000`
Frontend: `http://localhost:3000`
API Docs: `http://localhost:8000/docs`

### Run Tests

```bash
# All tests with Allure report
docker-compose exec backend pytest --alluredir=allure-results

# Specific test suite
docker-compose exec backend pytest tests/unit/ -v
docker-compose exec backend pytest tests/integration/ -v
docker-compose exec backend pytest tests/e2e/ -v

# Smoke tests
docker-compose exec backend pytest -m smoke -v

# Regression tests
docker-compose exec backend pytest -m regression -v

# With coverage
docker-compose exec backend pytest --cov=app --cov-report=html
```

---

## 🔬 Testing Architecture

### Testing Pyramid

```
        E2E (gRPC, WebSocket)          ▲
       /                    \           │
      /   Integration Tests   \         │ Coverage
     /  (API, Database, Cache)  \       │
    /_______________________ \  │
   /    Unit Tests           \ │▼
  /____________________________\
```

### Test Types

| Type | Count | Tools | Focus |
|------|-------|-------|-------|
| **Unit** | ~50 | pytest, hypothesis | Business logic, utilities |
| **Integration** | ~30 | pytest, testcontainers | API endpoints, DB operations |
| **E2E** | ~20 | pytest-asyncio, gRPC | Full workflows, user scenarios |
| **Smoke** | ~15 | Marked with `@pytest.mark.smoke` | Critical paths |
| **Regression** | ~85 | All tests with `@pytest.mark.regression` | Stability across versions |

### Design Patterns

- **AAA Pattern** (Arrange, Act, Assert)
- **Page Object Model** (API endpoint objects)
- **Factory Pattern** (Test data generation)
- **Fixture Pattern** (Shared setup/teardown)
- **Parametrization** (Test coverage optimization)

---

## 🔧 Technology Stack

### Backend
- **FastAPI** — Web framework
- **gRPC** — High-performance RPC
- **WebSocket** — Real-time communication
- **PostgreSQL** — Primary database
- **Redis** — Caching layer
- **SQLAlchemy** — ORM
- **Pydantic** — Data validation

### Testing
- **pytest** — Test framework
- **pytest-asyncio** — Async test support
- **pytest-cov** — Coverage analysis
- **hypothesis** — Property-based testing
- **HTTPX** — Async HTTP client
- **grpcio** — gRPC client
- **docker** — Containerization for test isolation

### Frontend
- **React 18** — UI library
- **TypeScript** — Type safety
- **Vite** — Build tool
- **Axios** — HTTP client

### DevOps
- **Docker** — Containerization
- **GitHub Actions** — CI/CD
- **Allure** — Test reporting
- **pytest-xdist** — Parallel test execution

---

## 📊 CI/CD Workflow

### GitHub Actions
- ✅ Runs on every PR and push to main
- ✅ Unit → Integration → E2E tests
- ✅ Code coverage reports
- ✅ Allure reports generated
- ✅ Docker image builds

```yaml
Trigger → Lint → Unit Tests → Integration Tests → E2E Tests → Allure Report
```

---

## 📚 Documentation

- **[TESTING.md](docs/TESTING.md)** — Testing strategy, patterns, best practices
- **[API.md](docs/API.md)** — REST, gRPC, WebSocket endpoints
- **[SETUP.md](docs/SETUP.md)** — Development environment setup
- **[RU Docs](docs/ru/)** — Russian language documentation

---

## 🏆 Key Features Demonstrated

✅ **Testing Expertise**
- Complete test pyramid implementation
- Smoke & regression test organization
- Parametrized tests for efficiency
- Async test handling
- Database transaction testing

✅ **Code Quality**
- 85%+ code coverage
- Type hints throughout
- Docstrings and comments (minimal, purposeful)
- PEP 8 compliance
- Pre-commit hooks

✅ **Best Practices**
- Factory patterns for test data
- Fixture composition
- Test isolation (each test is independent)
- Clear test naming (describe what, why, expected)
- AAA pattern consistency

✅ **Production Readiness**
- Docker multi-stage builds
- Environment configuration management
- Health checks
- Graceful shutdown
- Error handling and logging

---

## 💡 Usage Scenarios

### For Job Interviews
Show this project to demonstrate:
- "I've built a full-stack application with complete test coverage"
- "Here's how I structure tests at scale"
- "This is my CI/CD pipeline and test reporting"

### For Freelance Bids
Link to repository to show:
- Testing standards you maintain
- Architecture decisions and rationale
- DevOps and containerization skills
- Full project lifecycle management

### For Learning
Use as reference for:
- How to organize pytest projects
- Implementing test pyramids correctly
- Async/gRPC testing patterns
- Docker-based test environments

---

## 🤝 Contributing

This is a portfolio project. If you'd like to use it as a base for your own project:

1. Fork the repository
2. Remove/modify project-specific code
3. Adapt tests to your business logic
4. Deploy your version

---

## 📞 Contact

- **Email**: nikita.dronov.a@gmail.com
- **Twitter**: @DronovNA
- **Portfolio**: [GitHub](https://github.com/DronovNA)

---

## 📄 License

MIT License — feel free to use this project as reference or base for your own work.

---

**Last Updated**: December 2025  
**Python Version**: 3.11+  
**Status**: Active Development