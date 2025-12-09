import pytest
from selene import browser, have, be
from selene.support.shared import browser as shared_browser
import time

@pytest.mark.ui
class TestTasksSelene:
    """UI tests using Selene (simplified Selenium)"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        shared_browser.config.base_url = "http://localhost:3000"
        shared_browser.config.timeout = 10
        shared_browser.config.window_width = 1280
        shared_browser.config.window_height = 1024
        yield
        shared_browser.quit()
    
    def test_create_task_selene(self):
        """Test creating task using Selene"""
        browser.open("/")
        browser.element("#task-title").type("Selene Test Task")
        browser.element("#create-task-btn").click()
        browser.element(".task-title").should(have.text("Selene Test Task"))
    
    def test_task_list_visibility(self):
        """Test task list is visible after creation"""
        browser.open("/")
        browser.element("#task-title").type("Visibility Test")
        browser.element("#create-task-btn").click()
        browser.element(".task-item").should(be.visible)
    
    def test_checkbox_state_change(self):
        """Test checkbox changes task state"""
        browser.open("/")
        browser.element("#task-title").type("Checkbox State")
        browser.element("#create-task-btn").click()
        
        time.sleep(0.5)
        browser.element(".task-checkbox").click()
        time.sleep(0.5)
        
        browser.element(".task-item.completed").should(be.visible)
    
    def test_form_clear_after_submit(self):
        """Test form clears after submission"""
        browser.open("/")
        browser.element("#task-title").type("Clear Test")
        browser.element("#create-task-btn").click()
        
        time.sleep(0.5)
        browser.element("#task-title").should(have.value(""))
    
    def test_header_present(self):
        """Test page header is present"""
        browser.open("/")
        browser.element(".app-header h1").should(have.text("Task Manager"))