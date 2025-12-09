# Testing Strategy & Best Practices

## Overview

This document outlines the comprehensive testing approach used in the Advanced Test Project, demonstrating professional-grade testing practices.

## Testing Pyramid

```
        E2E Tests (5-10%)
         /           \
        /  Integration \        (15-20%)
       /   Tests        \
      /___________________\
     /    Unit Tests     \  (70-80%)
```

### Unit Tests (70-80%)
**Location**: `backend/tests/unit/`

- **Focus**: Business logic, utilities, validators
- **Framework**: pytest + hypothesis
- **Tools**: unittest.mock for dependencies
- **Coverage Target**: 90%+

**Example**:
```python
@pytest.mark.unit
class TestUserService:
    @pytest.mark.asyncio
    async def test_create_user_success(self):
        """Test successful user creation"""
        db_mock = AsyncMock()
        service = UserService(db_mock)
        
        user_data = UserCreate(
            email="test@example.com",
            username="testuser",
            password="password123"
        )
        
        result = await service.create_user(user_data)
        db_mock.add.assert_called_once()
```

### Integration Tests (15-20%)
**Location**: `backend/tests/integration/`

- **Focus**: API endpoints, database operations, external services
- **Framework**: pytest + httpx (async HTTP client)
- **Database**: SQLite in-memory for isolation
- **Validation**: Full request/response cycles

**Example**:
```python
@pytest.mark.integration
class TestUserEndpoints:
    @pytest.mark.smoke
    async def test_create_user_endpoint(self, test_client):
        """Test creating user via REST endpoint"""
        payload = {
            "email": "integration@example.com",
            "username": "integrationuser",
            "password": "password123"
        }
        
        response = await test_client.post("/api/v1/users/", json=payload)
        
        assert response.status_code == 201
        assert response.json()["email"] == "integration@example.com"
```

### E2E Tests (5-10%)
**Location**: `backend/tests/e2e/`

- **Focus**: Complete workflows across multiple endpoints
- **Framework**: pytest + async
- **Scenario**: User creation → Task creation → Task update
- **Validation**: Full business process success

**Example**:
```python
@pytest.mark.e2e
class TestUserWorkflow:
    @pytest.mark.smoke
    async def test_complete_user_lifecycle(self, test_client):
        """Test complete user creation and retrieval workflow"""
        # Create user
        create_response = await test_client.post(
            "/api/v1/users/",
            json={"email": "e2e@example.com", ...}
        )
        user_id = create_response.json()["id"]
        
        # Retrieve user
        get_response = await test_client.get(f"/api/v1/users/{user_id}")
        assert get_response.status_code == 200
```

## Test Types

### Smoke Tests
**Marker**: `@pytest.mark.smoke`
**Purpose**: Verify critical functionality works
**Run**: Before every deployment
**Count**: ~15 tests

```bash
pytest -m smoke -v
```

### Regression Tests
**Marker**: `@pytest.mark.regression`
**Purpose**: Ensure new changes don't break existing functionality
**Run**: Full test suite
**Count**: ~85 tests

```bash
pytest -m regression -v
```

## Design Patterns

### 1. AAA Pattern (Arrange, Act, Assert)

Every test follows this structure:

```python
def test_example():
    # ARRANGE: Set up test data and mocks
    mock_db = AsyncMock()
    service = UserService(mock_db)
    user_data = UserCreate(email="test@example.com", ...)
    
    # ACT: Execute the function being tested
    result = await service.create_user(user_data)
    
    # ASSERT: Verify the results
    assert result.email == "test@example.com"
    mock_db.add.assert_called_once()
```

### 2. Factory Pattern (Test Data Generation)

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

### 3. Fixture Pattern (Shared Setup/Teardown)

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

### 4. Page Object Pattern (API Objects)

Although this is for UI testing, we apply the concept to API:

```python
class UserAPI:
    def __init__(self, client):
        self.client = client
    
    async def create_user(self, email, username, password):
        return await self.client.post(
            "/api/v1/users/",
            json={"email": email, "username": username, "password": password}
        )
```

## Parametrization

Reduce code duplication with parametrized tests:

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

## Test Isolation

Each test is completely independent:

- **Database**: In-memory SQLite, cleaned between tests
- **Mocks**: Fresh mocks for each test
- **Fixtures**: Session-scoped setup, function-scoped teardown
- **No test dependencies**: Tests can run in any order

## Running Tests

### All tests
```bash
pytest -v
```

### Specific test suite
```bash
pytest tests/unit/ -v          # Unit tests only
pytest tests/integration/ -v   # Integration tests only
pytest tests/e2e/ -v           # E2E tests only
```

### By marker
```bash
pytest -m smoke -v             # Smoke tests
pytest -m regression -v        # Regression tests
pytest -m unit -v              # Unit tests
```

### With coverage
```bash
pytest --cov=app --cov-report=html
```

### Parallel execution
```bash
pytest -n auto                 # Uses all CPU cores
```

### Allure reporting
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## CI/CD Integration

The project uses GitHub Actions with automated test execution:

1. **Unit Tests** (fast, no dependencies)
2. **Integration Tests** (requires DB/Redis)
3. **E2E Tests** (full workflow validation)
4. **Coverage Reports** (codecov.io integration)
5. **Allure Reports** (artifact generation)

## Best Practices

✅ **DO**:
- One assertion per test (or logically related assertions)
- Clear, descriptive test names
- Use fixtures for shared setup
- Mock external dependencies
- Test error cases, not just happy paths
- Use parametrization to reduce duplication
- Keep tests simple and readable

❌ **DON'T**:
- Share state between tests
- Use sleep() for timing (use fixtures instead)
- Test multiple behaviors in one test
- Have complex logic in tests
- Skip tests without a reason
- Hard-code test data

## Coverage Goals

- **Unit**: 90%+
- **Integration**: 80%+
- **Overall**: 85%+
- **Critical paths**: 100%

## Continuous Improvement

Regularly review:
- Test execution time (target: < 10 seconds for unit tests)
- Coverage trends (should never decrease)
- Flaky tests (identify and fix immediately)
- Test maintenance burden (refactor duplicated test code)
