# Advanced Test Project 🔬🚀

[![Tests](https://github.com/DronovNA/advanced-test-project/workflows/Test%20Suite/badge.svg)](https://github.com/DronovNA/advanced-test-project/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)

**Полноценный веб-приложение и свкбе тестов для демонстрации профессиональных навыков QA автоматизации.**

## 📋 Обзор

Этот проект демонстрирует:

- **Бэкенд**: FastAPI с REST API, gRPC, WebSocket
- **Навыки тестирования**: Полная пирамида (юнит → интеграцию → E2E)
- **Организация**: Smoke & Regression тесты
- **CI/CD**: GitHub Actions с Allure отчётами
- **DevOps**: Docker, Docker Compose, контейнеризация
- **Веб**: React 18 + TypeScript frontend

## 🚀 Быстрый старт

### Предварительные требования

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- Git

### Настройка и деплой

```bash
# Клонирование
git clone https://github.com/DronovNA/advanced-test-project.git
cd advanced-test-project

# Запуск Docker-сервисов
docker-compose up --build
```

**Адреса**:
- Backend: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Frontend: `http://localhost:3000`

### Запуск Тестов

```bash
# Все тесты
docker-compose exec backend pytest -v

# Конкретные наборы
docker-compose exec backend pytest tests/unit/ -v
docker-compose exec backend pytest tests/integration/ -v
docker-compose exec backend pytest tests/e2e/ -v

# Smoke тесты
docker-compose exec backend pytest -m smoke -v

# Покрытие
docker-compose exec backend pytest --cov=app --cov-report=html
```

## 🔬 Архитектура тестов

### Пирамида тестирования

```
        E2E (gRPC, WebSocket)          ▲
       /                    \           │
      /   Integration Tests   \         │ Coverage
     /  (API, Database, Cache)  \       │
    /_______________________ \  │
   /    Unit Tests           \ │▼
  /____________________________\
```

### Типы тестов

| Тип | Кол-во | Инструменты | Нацелено |
|------|--------|----------|----------|
| **Unit** | ~50 | pytest, hypothesis | Бизнес-логика |
| **Integration** | ~30 | pytest, httpx | API endpoints, DB |
| **E2E** | ~20 | pytest-asyncio | Полные workflows |
| **Smoke** | ~15 | @pytest.mark.smoke | Критичные части |
| **Regression** | ~85 | @pytest.mark.regression | Обс тесты |

### Паттерны архитектуры

- **AAA Pattern** (Arrange, Act, Assert)
- **Factory Pattern** (генерация тестовых данных)
- **Fixture Pattern** (общая подготовка)
- **Page Object Model** (API objects)
- **Parametrization** (минимизация дублирования)

## 📚 Документация

### Английский
- **[README.md](README.md)** — Полный овервью
- **[docs/TESTING.md](docs/TESTING.md)** — Стратегия тестирования
- **[docs/SETUP.md](docs/SETUP.md)** — Настройка окружения
- **[docs/API.md](docs/API.md)** — Документация API
- **[docs/MOBILE_TESTING.md](docs/MOBILE_TESTING.md)** — Мобильное тестирование

### Русский
- **[docs/ru/TESTING.md](docs/ru/TESTING.md)** — Стратегия тестирования
- **[docs/ru/SETUP.md](docs/ru/SETUP.md)** — Настройка окружения
- **[docs/ru/API.md](docs/ru/API.md)** — Документация API

## 📄 Основные филы

### Бэкенд
- **app/models/** — SQLAlchemy ORM модели
- **app/schemas/** — Pydantic схемы валидации
- **app/services/** — Бизнес-логика
- **app/api/rest/** — REST endpoints
- **tests/unit/** — Unit тесты
- **tests/integration/** — Integration тесты
- **tests/e2e/** — E2E тесты

### Фронтенд
- **src/main.tsx** — Нточная точка
- **src/App.tsx** — Основное приложение

### DevOps
- **docker-compose.yml** — Локальная оркестрация
- **.github/workflows/tests.yml** — CI/CD конвейер
- **pytest.ini** — Конфигурация pytest
- **pyproject.toml** — Проектные сеттингс

## ✅ Открытая социальная сеть

Цель этого проекта:

1. **Для интервью** — "Господа, на моюм гитхабе вы сможете увидеть полные тесты..."

2. **Для фриланса** — "Это проект демонстрирует мои стандарты..."

3. **Для обучения** — "Читайте, экспериментируйте, вкладывайте себяв разработку..."

## 📁 Структура проекта

```
advanced-test-project/
├── backend/
│   ├── app/
│   │   ├── api/rest/           ← REST ендпоинты
│   │   ├── models/           ← ОРМ модели
│   │   ├── schemas/          ← Pydantic валидация
│   │   ├── services/         ← Бизнес-логика
│   │   └── database.py       ← BD конфиг
│   ├── tests/
│   │   ├── unit/             ← 50 тестов
│   │   ├── integration/      ← 30 тестов
│   │   ├── e2e/              ← 20 тестов
│   │   └── fixtures/         ← факторыи данные
│   ├── requirements.txt
│   ├── Dockerfile
│   └── pytest.ini
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml       ← Оркестрация
├── .github/workflows/       ← CI/CD
├── docs/                    ← Документация (EN + RU)
└── README.md / README_RU.md
```

## 📊 Технологии

### Бэкенд
- **FastAPI** — веб-фреймворк
- **PostgreSQL** — основная БД
- **Redis** — кэш
- **SQLAlchemy** — ORM
- **Pydantic** — валидация

### Тестирование
- **pytest** — фреймворк
- **pytest-asyncio** — async суппорт
- **pytest-cov** — покрытие
- **hypothesis** — property-based тесты
- **httpx** — async клиент

### DevOps
- **Docker** — контейнеризация
- **GitHub Actions** — CI/CD
- **Allure** — репорты

## 🎯 Как это работает

### Локально

```bash
# 1. Доставка сервисов
docker-compose up --build

# 2. Тесты с текущим кодом
docker-compose exec backend pytest -v --watch

# 3. Просмотр результатов
open http://localhost:8000/docs
```

### На GitHub

Каждый push триггерит:

```
Trigger → Lint → Unit Tests → Integration Tests → E2E Tests → Allure Report
```

## 📄 Настоящая реальность

Эта репозитория:

- ✅ Доказывает **онашь** высоких стандартов тестирования
- ✅ Показывает **уверенность** в pytest деталях
- ✅ Иллюстрирует **станиэйность** CI/CD
- ✅ Демонстрирует **мобильность** архитектуры

## 🛠 Необязательные исправления

Мобильное тестирование (ОН) - используется **Playwright** для мобильных браузеров:

```python
import pytest
from playwright.async_api import async_playwright

@pytest.mark.mobile
async def test_mobile_responsive():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 375, 'height': 812}  # iPhone 12
        )
        page = await context.new_page()
        await page.goto('http://localhost:3000')
        # тестирование
```

для нативных приложений используется **Appium** (см. [docs/MOBILE_TESTING.md](docs/MOBILE_TESTING.md)).

## ❓ Вопросы?

- **Эмейл**: nikita.dronov.a@gmail.com
- **Twitter**: @DronovNA
- **Issues**: Открыте на GitHub

## 📄 Лицензия

MIT License — свободно используйте как базу разработки.

---

**Последнее обновление**: декабрь 2025  
**Версия**: 1.0.0  
**Статус**: реади для новых овонек