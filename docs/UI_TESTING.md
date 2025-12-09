# UI Testing Guide

This project includes comprehensive UI testing using three modern frameworks:

## Frameworks Used

### 1. Playwright
**Best for:** Cross-browser testing, modern async API

```python
# Example test
async def test_create_task(browser_page):
    await browser_page.goto("http://localhost:3000")
    await browser_page.fill("#task-title", "New Task")
    await browser_page.click("#create-task-btn")
    assert await browser_page.text_content(".task-title") == "New Task"
```

### 2. Selenium WebDriver
**Best for:** Industry standard, wide browser support

```python
# Example test
def test_create_task(driver):
    driver.get("http://localhost:3000")
    driver.find_element(By.ID, "task-title").send_keys("New Task")
    driver.find_element(By.ID, "create-task-btn").click()
    assert "New Task" in driver.page_source
```

### 3. Selene
**Best for:** Clean syntax, less boilerplate

```python
# Example test
def test_create_task():
    browser.open("/")
    browser.element("#task-title").type("New Task")
    browser.element("#create-task-btn").click()
    browser.element(".task-title").should(have.text("New Task"))
```

## Running UI Tests

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install
```

### Run All UI Tests
```bash
pytest tests/ui/ -v
```

### Run Specific Framework
```bash
# Playwright tests only
pytest tests/ui/test_tasks_playwright.py -v

# Selenium tests only
pytest tests/ui/test_tasks_selenium.py -v

# Selene tests only
pytest tests/ui/test_tasks_selene.py -v
```

### Run with Markers
```bash
# Run all UI tests
pytest -m ui -v

# Run smoke UI tests
pytest -m "ui and smoke" -v
```

## Test Structure

```
tests/ui/
├── conftest.py              # UI test fixtures
├── test_tasks_playwright.py # Playwright tests (7 tests)
├── test_tasks_selenium.py   # Selenium tests (7 tests)
└── test_tasks_selene.py     # Selene tests (5 tests)
```

## CI/CD Integration

UI tests run in GitHub Actions with:
- Headless Chrome
- Xvfb for display simulation
- Automatic screenshot capture on failure

## Best Practices

1. **Use explicit waits**
   ```python
   await page.wait_for_selector(".task-item")
   ```

2. **Use data-testid attributes**
   ```html
   <button data-testid="create-task-btn">Create</button>
   ```

3. **Keep tests independent**
   - Each test should work in isolation
   - Clean up data after tests

4. **Use Page Object Model** (for larger projects)
   ```python
   class TaskPage:
       def __init__(self, page):
           self.page = page
       
       async def create_task(self, title):
           await self.page.fill("#task-title", title)
           await self.page.click("#create-task-btn")
   ```

## Troubleshooting

### Playwright Issues
```bash
# Reinstall browsers
python -m playwright install --force
```

### Selenium Issues
```bash
# Update ChromeDriver
pip install --upgrade selenium
```

### Headless Mode
All tests run in headless mode by default. To see the browser:

```python
# Playwright
browser = await p.chromium.launch(headless=False)

# Selenium
options.add_argument("--headless")  # Remove this line
```