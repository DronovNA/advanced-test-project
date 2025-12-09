# Стратегия Тестирования & Лучшие Практики

## Обзор

В этом документе описан комплексный подход к тестированию, используемый в Advanced Test Project, демонстрирующий профессиональные практики тестирования.

## Пирамида Тестирования

```
        E2E Тесты (5-10%)
         /           \
        /  Интеграционные (15-20%)
       /   Тесты        \
      /___________________\
     /    Unit Тесты    \  (70-80%)
```

### Unit Тесты (70-80%)
**Расположение**: `backend/tests/unit/`

- **Фокус**: Бизнес-логика, утилиты, валидаторы
- **Фреймворк**: pytest + hypothesis
- **Инструменты**: unittest.mock для зависимостей
- **Целевое покрытие**: 90%+

### Интеграционные Тесты (15-20%)
**Расположение**: `backend/tests/integration/`

- **Фокус**: API endpoints, операции БД, внешние сервисы
- **Фреймворк**: pytest + httpx (async HTTP клиент)
- **БД**: SQLite в памяти для изоляции
- **Валидация**: Полные циклы запрос/ответ

### E2E Тесты (5-10%)
**Расположение**: `backend/tests/e2e/`

- **Фокус**: Полные бизнес-процессы через несколько endpoints
- **Фреймворк**: pytest + async
- **Сценарий**: Создание пользователя → Создание задачи → Обновление задачи
- **Валидация**: Успешность полного бизнес-процесса

## Типы Тестов

### Smoke Тесты
**Маркер**: `@pytest.mark.smoke`
**Назначение**: Проверить работу критичного функционала
**Запуск**: Перед каждым развертыванием
**Количество**: ~15 тестов

```bash
pytest -m smoke -v
```

### Regression Тесты
**Маркер**: `@pytest.mark.regression`
**Назначение**: Убедиться, что новые изменения не сломали существующий функционал
**Запуск**: Полный набор тестов
**Количество**: ~85 тестов

```bash
pytest -m regression -v
```

## Паттерны Проектирования

### 1. AAA Паттерн (Arrange, Act, Assert)

Каждый тест следует этой структуре:

```python
def test_example():
    # ARRANGE: Подготовка данных и моков
    mock_db = AsyncMock()
    service = UserService(mock_db)
    user_data = UserCreate(email="test@example.com", ...)
    
    # ACT: Выполнение тестируемой функции
    result = await service.create_user(user_data)
    
    # ASSERT: Проверка результатов
    assert result.email == "test@example.com"
    mock_db.add.assert_called_once()
```

### 2. Factory Паттерн (Генерация Тестовых Данных)

```python
class UserFactory:
    @classmethod
    def create(cls, email="test@example.com", username="testuser"):
        return User(
            email=email,
            username=username,
            hashed_password=hash_password("password")
        )

user = UserFactory.create(email="custom@example.com")
```

### 3. Fixture Паттерн (Общая Подготовка/Очистка)

```python
@pytest.fixture
async def sample_user(test_session):
    user = User(...)
    test_session.add(user)
    await test_session.commit()
    return user

def test_example(sample_user):
    assert sample_user.id is not None
```

## Параметризация

Сокращение дублирования кода с параметризованными тестами:

```python
@pytest.mark.parametrize("email,expected_valid", [
    ("valid@example.com", True),
    ("invalid-email", False),
    ("", False),
])
def test_email_validation(email, expected_valid):
    try:
        UserCreate(email=email, username="test", password="pass")
        assert expected_valid is True
    except ValidationError:
        assert expected_valid is False
```

## Изоляция Тестов

Каждый тест полностью независим:

- **БД**: In-memory SQLite, очищается между тестами
- **Моки**: Свежие моки для каждого теста
- **Fixtures**: Session-scoped setup, function-scoped teardown
- **Нет зависимостей**: Тесты могут запускаться в любом порядке

## Запуск Тестов

### Все тесты
```bash
pytest -v
```

### Конкретный набор
```bash
pytest tests/unit/ -v          # Только unit
pytest tests/integration/ -v   # Только интеграционные
pytest tests/e2e/ -v           # Только E2E
```

### По маркерам
```bash
pytest -m smoke -v             # Smoke тесты
pytest -m regression -v        # Regression тесты
```

### С покрытием
```bash
pytest --cov=app --cov-report=html
```

### Параллельное выполнение
```bash
pytest -n auto                 # Использует все ядра CPU
```

### Allure отчёты
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Интеграция с CI/CD

Проект использует GitHub Actions с автоматическим запуском тестов:

1. **Unit Тесты** (быстро, нет зависимостей)
2. **Интеграционные Тесты** (требует БД/Redis)
3. **E2E Тесты** (полная валидация бизнес-процесса)
4. **Coverage Отчёты** (codecov.io интеграция)
5. **Allure Отчёты** (генерация артефактов)

## Лучшие Практики

✅ **ДЕЛАТЬ**:
- Одно утверждение на тест (или логически связанные)
- Ясные, описательные имена тестов
- Использование fixtures для общей подготовки
- Мокирование внешних зависимостей
- Тестирование случаев ошибок, а не только счастливых путей
- Параметризация для сокращения дублирования
- Простые и читаемые тесты

❌ **НЕ ДЕЛАТЬ**:
- Общее состояние между тестами
- sleep() для синхронизации (используйте fixtures)
- Несколько поведений в одном тесте
- Сложную логику в тестах
- Пропускать тесты без причины
- Жёсткие тестовые данные

## Цели Покрытия

- **Unit**: 90%+
- **Integration**: 80%+
- **Общее**: 85%+
- **Критичные пути**: 100%
