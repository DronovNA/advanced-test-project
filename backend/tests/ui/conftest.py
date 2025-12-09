import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def playwright():
    """Start Playwright for the test session"""
    async with async_playwright() as p:
        yield p

@pytest.fixture
async def browser(playwright):
    """Launch browser instance"""
    browser = await playwright.chromium.launch(headless=True)
    yield browser
    await browser.close()

@pytest.fixture
async def page(browser):
    """Create new page"""
    page = await browser.new_page()
    yield page
    await page.close()