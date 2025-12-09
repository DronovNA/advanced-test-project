# Contribution Guidelines

## For Portfolio Use

This project is designed as a portfolio/demonstration project. If you'd like to use it as a base:

1. **Fork** the repository
2. **Remove** references to "Advanced Test Project"
3. **Replace** with your own project domain
4. **Adapt** tests to your specific business logic
5. **Deploy** your version

## Code Standards

- **Python**: 3.11+
- **Type Hints**: Required for all functions
- **Testing**: All new code must have tests
- **Coverage**: Maintain 85%+ coverage
- **Formatting**: Black (line length: 100)
- **Linting**: flake8
- **Imports**: isort

## Pre-commit Setup

```bash
pip install pre-commit
pre-commit install
```

This will automatically format and lint your code before commits.

## Test Requirements

- New features must include unit + integration tests
- All tests must pass locally before submitting
- Tests must be marked appropriately (@pytest.mark.unit, etc.)
- No test skips without justification

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes with tests
3. Run full test suite: `pytest -v`
4. Check coverage: `pytest --cov=app`
5. Commit with clear message: `git commit -m "Add: clear description"`
6. Push and create PR

## Questions?

Open an issue or contact: nikita.dronov.a@gmail.com
