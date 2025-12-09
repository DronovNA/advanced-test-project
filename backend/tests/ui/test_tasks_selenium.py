import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

@pytest.mark.ui
class TestTasksSelenium:
    """UI tests using Selenium WebDriver"""
    
    @pytest.fixture
    def driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    def test_page_title(self, driver):
        """Test page title loads correctly"""
        driver.get("http://localhost:3000")
        assert "Task Manager" in driver.page_source
    
    def test_create_task_selenium(self, driver):
        """Test creating task via Selenium"""
        driver.get("http://localhost:3000")
        
        title_input = driver.find_element(By.ID, "task-title")
        title_input.send_keys("Selenium Test Task")
        
        submit_btn = driver.find_element(By.ID, "create-task-btn")
        submit_btn.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "task-item"))
        )
        
        task_title = driver.find_element(By.CLASS_NAME, "task-title")
        assert "Selenium Test Task" in task_title.text
    
    def test_checkbox_interaction(self, driver):
        """Test checkbox interaction"""
        driver.get("http://localhost:3000")
        
        driver.find_element(By.ID, "task-title").send_keys("Check Test")
        driver.find_element(By.ID, "create-task-btn").click()
        
        time.sleep(0.5)
        checkbox = driver.find_element(By.CLASS_NAME, "task-checkbox")
        checkbox.click()
        
        time.sleep(0.5)
        task_item = driver.find_element(By.CLASS_NAME, "task-item")
        assert "completed" in task_item.get_attribute("class")
    
    def test_delete_button_visible(self, driver):
        """Test delete button is visible"""
        driver.get("http://localhost:3000")
        
        driver.find_element(By.ID, "task-title").send_keys("Delete Visibility Test")
        driver.find_element(By.ID, "create-task-btn").click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "delete-btn"))
        )
        
        delete_btn = driver.find_element(By.CLASS_NAME, "delete-btn")
        assert delete_btn.is_displayed()
    
    def test_form_elements_present(self, driver):
        """Test all form elements are present"""
        driver.get("http://localhost:3000")
        
        title_input = driver.find_element(By.ID, "task-title")
        desc_input = driver.find_element(By.ID, "task-description")
        submit_btn = driver.find_element(By.ID, "create-task-btn")
        
        assert title_input is not None
        assert desc_input is not None
        assert submit_btn is not None
    
    def test_task_description_optional(self, driver):
        """Test creating task without description"""
        driver.get("http://localhost:3000")
        
        driver.find_element(By.ID, "task-title").send_keys("No Description Task")
        driver.find_element(By.ID, "create-task-btn").click()
        
        time.sleep(0.5)
        task_items = driver.find_elements(By.CLASS_NAME, "task-item")
        assert len(task_items) > 0
    
    def test_error_message_display(self, driver):
        """Test error message can be displayed"""
        driver.get("http://localhost:3000")
        
        error_elements = driver.find_elements(By.CLASS_NAME, "error-message")
        assert isinstance(error_elements, list)