# Advanced Test Project

[![Tests](https://github.com/DronovNA/advanced-test-project/workflows/Test%20Suite/badge.svg)](https://github.com/DronovNA/advanced-test-project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)

**A comprehensive full-stack web application with production-grade test suite demonstrating advanced testing practices, UI automation, and modern web technologies.**

## 📋 Overview

This project showcases:
- **Backend**: FastAPI with REST API, gRPC, WebSocket
- **Frontend**: React Task Manager with full CRUD operations
- **Testing**: Complete pyramid (Unit → Integration → E2E → UI)
- **UI Automation**: Playwright, Selenium WebDriver, Selene
- **Database**: PostgreSQL + Redis caching
- **CI/CD**: GitHub Actions with Selenoid
- **Containerization**: Docker & Docker Compose

### 🎯 Target Audience
- QA Automation Engineers
- Full-stack developers
- DevOps engineers
- Teams evaluating test frameworks

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required
Docker & Docker Compose
Python 3.11+
Node.js 20+

# Optional (for local development)
PostgreSQL 15+
Redis 7+
```

### Setup

```bash
# Clone repository
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project

# Start all services
docker-compose up --build

# Access services
# Backend API: http://localhost:8000
# Frontend UI: http://localhost:3000
# API Docs: http://localhost:8000/docs
# Selenoid UI: http://localhost:8080
```

### Run Tests

```bash
# All tests
pytest tests/ -v

# By layer
pytest tests/unit/ -v              # Unit tests
pytest tests/integration/ -v       # Integration tests
pytest tests/e2e/ -v               # E2E tests
pytest tests/ui/ -v                # UI tests

# By technology
pytest tests/ui/test_tasks_playwright.py -v  # Playwright
pytest tests/ui/test_tasks_selenium.py -v    # Selenium
pytest tests/ui/test_tasks_selene.py -v      # Selene

# By markers
pytest -m smoke -v                 # Smoke tests
pytest -m regression -v            # Regression tests
pytest -m ui -v                    # All UI tests

# With coverage
pytest --cov=app --cov-report=html

# With Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🔬 Testing Architecture

### Testing Pyramid

```
       E2E (Workflows)              ▲
      /                \            │
     /  Integration     \           │ Complexity
    /   (API, DB)       \           │
   /____________________\           │
  /     Unit Tests       \          │
 /_______________________\          ▼
```

### Test Distribution

| Type | Count | Tools | Focus |
|------|-------|-------|-------|
| **Unit** | 20 | pytest, hypothesis | Business logic |
| **Integration** | 15 | pytest-asyncio, httpx | API endpoints |
| **E2E** | 10 | pytest, gRPC | Full workflows |
| **UI** | 19 | Playwright, Selenium, Selene | User interface |
| **Total** | 64 | — | — |

### UI Testing Frameworks

#### Playwright (7 tests)
- Modern async API
- Auto-wait capabilities
- Cross-browser support
- Screenshot/video recording

```python
async def test_create_task_ui(browser_page):
    await browser_page.goto("http://localhost:3000")
    await browser_page.fill("#task-title", "New Task")
    await browser_page.click("#create-task-btn")
    assert await browser_page.text_content(".task-title") == "New Task"
```

#### Selenium WebDriver (7 tests)
- Industry standard
- Wide browser support
- Mature ecosystem
- Cloud grid integration

```python
def test_create_task_selenium(driver):
    driver.get("http://localhost:3000")
    driver.find_element(By.ID, "task-title").send_keys("New Task")
    driver.find_element(By.ID, "create-task-btn").click()
    assert "New Task" in driver.page_source
```

#### Selene (5 tests)
- Clean API
- Less boilerplate
- Built-in smart waits
- Concise syntax

```python
def test_create_task_selene():
    browser.open("/")
    browser.element("#task-title").type("New Task")
    browser.element("#create-task-btn").click()
    browser.element(".task-title").should(have.text("New Task"))
```

---

## 🔧 Technology Stack

### Backend
- **FastAPI** — Modern web framework
- **gRPC** — High-performance RPC
- **WebSocket** — Real-time updates
- **PostgreSQL** — Primary database
- **Redis** — Caching layer
- **SQLAlchemy** — Async ORM
- **Pydantic** — Data validation

### Frontend
- **React 18** — UI library
- **TypeScript** — Type safety
- **Vite** — Build tool
- **Axios** — HTTP client

### Testing
- **pytest** — Test framework
- **Playwright** — Modern UI automation
- **Selenium** — Classic UI automation
- **Selene** — Simplified Selenium
- **pytest-asyncio** — Async support
- **pytest-cov** — Coverage
- **hypothesis** — Property-based testing
- **Allure** — Test reporting

### DevOps
- **Docker** — Containerization
- **GitHub Actions** — CI/CD
- **Selenoid** — Browser automation grid
- **pytest-xdist** — Parallel execution

---

## 📊 CI/CD Pipeline

### GitHub Actions Workflows

#### Backend Tests
```
Trigger → Lint → Unit → Integration → E2E → Allure Report
```

#### UI Tests
```
Trigger → Setup Browsers → Build Frontend → Run Playwright → Run Selenium → Run Selene → Upload Artifacts
```

### Selenoid Integration
- Isolated browser sessions
- Video recording on failure
- Parallel test execution
- Cross-browser testing

---

## 📁 Project Structure

```
advanced-test-project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── rest/          # REST endpoints
│   │   │   ├── grpc/          # gRPC services
│   │   │   └── websocket/     # WebSocket handlers
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   └── config.py          # Configuration
│   ├── tests/
│   │   ├── unit/              # Unit tests
│   │   ├── integration/       # Integration tests
│   │   ├── e2e/               # E2E tests
│   │   ├── ui/                # UI tests (Playwright/Selenium/Selene)
│   │   └── conftest.py        # Test fixtures
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── types/             # TypeScript types
│   │   ├── App.tsx            # Main app
│   │   └── App.css            # Styles
│   └── package.json
├── docs/
│   ├── TESTING.md             # Testing guide (EN)
│   ├── UI_TESTING.md          # UI testing guide
│   ├── GRPC.md                # gRPC guide
│   ├── WEBSOCKET.md           # WebSocket guide
│   └── ru/                    # Russian docs
├── .github/workflows/
│   ├── tests.yml              # Backend tests
│   └── ui-tests.yml           # UI tests
├── docker-compose.yml
├── selenoid/
│   └── browsers.json          # Selenoid config
└── pytest.ini
```

---

## 🏆 Key Features

### ✅ Testing Excellence
- **64 automated tests** across all layers
- **80%+ code coverage**
- **UI automation** with 3 frameworks
- **Parallel test execution**
- **Allure reports** with rich artifacts
- **CI/CD integration** with GitHub Actions

### ✅ Real Application
- **Task Manager** with full CRUD
- **REST API** with Swagger docs
- **gRPC API** for microservices
- **WebSocket** for real-time updates
- **React UI** with TypeScript

### ✅ Production Patterns
- **AAA test pattern**
- **Page Object Model** (for UI tests)
- **Factory pattern** (test data)
- **Fixture composition**
- **Test isolation**

### ✅ DevOps Ready
- **Docker multi-stage builds**
- **Health checks**
- **Environment configuration**
- **Logging and monitoring hooks**
- **Graceful shutdown**

---

## 📚 Documentation

- **[UI_TESTING.md](docs/UI_TESTING.md)** — Playwright, Selenium, Selene guides
- **[GRPC.md](docs/GRPC.md)** — gRPC API documentation
- **[WEBSOCKET.md](docs/WEBSOCKET.md)** — WebSocket guide
- **[Russian Docs](docs/ru/)** — Full documentation in Russian

---

## 💡 Use Cases

### 👨‍💼 For Job Interviews
"I built a full-stack application with:
- 64 automated tests (UI + API + Unit)
- Three UI automation frameworks
- CI/CD with Selenoid
- 80%+ test coverage"

### 💼 For Portfolio
- Demonstrates modern testing practices
- Shows full-stack capabilities
- Proves DevOps knowledge
- Real working application

### 📖 For Learning
- Reference for test architecture
- UI automation patterns
- Async testing examples
- Docker-based test environments

---

## 🤝 Technologies Demonstrated

✅ Python (FastAPI, pytest, SQLAlchemy)  
✅ JavaScript/TypeScript (React, Vite)  
✅ UI Automation (Playwright, Selenium, Selene)  
✅ API Testing (REST, gRPC, WebSocket)  
✅ Databases (PostgreSQL, Redis)  
✅ DevOps (Docker, GitHub Actions, Selenoid)  
✅ Test Design (Patterns, Best Practices)  

---

## 📞 Contact

- **Email**: nikita.dronov.a@gmail.com
- **GitHub**: [@DronovNA](https://github.com/DronovNA)
- **Location**: Málaga, Spain

---

## 📄 License

MIT License — Free to use as reference or template.

---

**Last Updated**: December 2025  
**Status**: Production Ready  
**Test Count**: 64 automated tests  
**Coverage**: 80%+