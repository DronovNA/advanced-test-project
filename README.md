# Advanced Test Project

[![Tests](https://github.com/DronovNA/advanced-test-project/workflows/Test%20Suite/badge.svg)](https://github.com/DronovNA/advanced-test-project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)

QA automation portfolio project with REST API, Task Manager UI, and comprehensive test suite.

## Overview

- **Backend**: FastAPI REST API
- **Frontend**: React Task Manager
- **Testing**: Unit, Integration, E2E, UI tests
- **Database**: PostgreSQL + Redis
- **CI/CD**: GitHub Actions

## Quick Start

```bash
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project
docker-compose up --build
```

Access:
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

## Run Tests

```bash
# Backend tests (CI automated)
docker-compose exec backend pytest tests/unit/ tests/integration/ tests/e2e/ -v

# UI tests (local only)
docker-compose exec backend pytest tests/ui/ -v

# Coverage
docker-compose exec backend pytest --cov=app --cov-report=html
```

## Test Suite

| Type | Count | Status |
|------|-------|--------|
| Unit | 15 | ✅ CI |
| Integration | 10 | ✅ CI |
| E2E | 5 | ✅ CI |
| UI (Playwright) | 7 | ⚠️ Local |
| UI (Selenium) | 7 | ⚠️ Local |
| UI (Selene) | 5 | ⚠️ Local |
| **Total** | **49** | - |

## Tech Stack

**Backend**: FastAPI, SQLAlchemy, PostgreSQL, Redis  
**Frontend**: React, TypeScript, Vite  
**Testing**: pytest, Playwright, Selenium, Selene  
**DevOps**: Docker, GitHub Actions

## Project Structure

```
backend/
├── app/
│   ├── api/rest/          # REST endpoints
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   └── main.py
├── tests/
│   ├── unit/              # 15 tests
│   ├── integration/       # 10 tests
│   ├── e2e/               # 5 tests
│   └── ui/                # 19 tests
frontend/
├── src/
│   ├── components/
│   └── App.tsx
```

## Documentation

- [UI Testing Guide](docs/UI_TESTING.md)

## Contact

Nikita Dronov  
Email: nikita.dronov.a@gmail.com  
GitHub: [@DronovNA](https://github.com/DronovNA)

## License

MIT