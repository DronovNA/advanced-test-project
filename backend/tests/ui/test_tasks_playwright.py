import pytest
from playwright.async_api import async_playwright, Page
import asyncio

@pytest.mark.ui
@pytest.mark.asyncio
class TestTasksPlaywright:
    """UI tests using Playwright"""
    
    @pytest.fixture
    async def browser_page(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            yield page
            await browser.close()
    
    async def test_create_task_ui(self, browser_page: Page):
        """Test creating task via UI"""
        await browser_page.goto("http://localhost:3000")
        
        await browser_page.fill("#task-title", "Playwright Test Task")
        await browser_page.fill("#task-description", "Created via Playwright")
        await browser_page.click("#create-task-btn")
        
        await browser_page.wait_for_selector(".task-item")
        task_title = await browser_page.text_content(".task-title")
        assert "Playwright Test Task" in task_title
    
    async def test_toggle_task_completion(self, browser_page: Page):
        """Test toggling task completion status"""
        await browser_page.goto("http://localhost:3000")
        
        await browser_page.fill("#task-title", "Toggle Test")
        await browser_page.click("#create-task-btn")
        await browser_page.wait_for_selector(".task-checkbox")
        
        checkbox = browser_page.locator(".task-checkbox").first
        await checkbox.click()
        
        await browser_page.wait_for_selector(".task-item.completed")
        is_completed = await browser_page.locator(".task-item.completed").count()
        assert is_completed > 0
    
    async def test_delete_task_ui(self, browser_page: Page):
        """Test deleting task via UI"""
        await browser_page.goto("http://localhost:3000")
        
        await browser_page.fill("#task-title", "Delete Me")
        await browser_page.click("#create-task-btn")
        await browser_page.wait_for_selector(".delete-btn")
        
        await browser_page.click(".delete-btn")
        await browser_page.wait_for_timeout(500)
        
        tasks_count = await browser_page.locator(".task-item").count()
        assert tasks_count == 0
    
    async def test_empty_state_display(self, browser_page: Page):
        """Test empty state message"""
        await browser_page.goto("http://localhost:3000")
        
        no_tasks_msg = await browser_page.text_content(".no-tasks")
        assert "No tasks yet" in no_tasks_msg
    
    async def test_task_form_validation(self, browser_page: Page):
        """Test form validation for empty title"""
        await browser_page.goto("http://localhost:3000")
        
        await browser_page.click("#create-task-btn")
        
        is_valid = await browser_page.evaluate("document.querySelector('#task-title').validity.valid")
        assert is_valid is False
    
    async def test_multiple_tasks_display(self, browser_page: Page):
        """Test displaying multiple tasks"""
        await browser_page.goto("http://localhost:3000")
        
        for i in range(3):
            await browser_page.fill("#task-title", f"Task {i+1}")
            await browser_page.click("#create-task-btn")
            await asyncio.sleep(0.3)
        
        tasks_count = await browser_page.locator(".task-item").count()
        assert tasks_count == 3
    
    async def test_task_with_description(self, browser_page: Page):
        """Test creating task with description"""
        await browser_page.goto("http://localhost:3000")
        
        await browser_page.fill("#task-title", "Task with Description")
        await browser_page.fill("#task-description", "This is a test description")
        await browser_page.click("#create-task-btn")
        
        await browser_page.wait_for_selector(".task-description")
        description = await browser_page.text_content(".task-description")
        assert "This is a test description" in description