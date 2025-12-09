# Mobile Testing Strategy (Appium)

## Overview

This document outlines the mobile testing approach for the Advanced Test Project using Appium and Selenium WebDriver.

## Current Status

The current version focuses on **API and backend testing**. Mobile testing would be implemented for a React Native or Flutter mobile companion app.

## Recommended Approach

### Option 1: Web-based Mobile Testing (Current Viable)

Test the responsive React frontend on mobile viewports:

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.mobile
class TestMobileResponsive:
    @pytest.fixture
    def mobile_driver(self):
        options = webdriver.ChromeOptions()
        # Mobile user agent
        options.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)')
        # Mobile viewport
        options.add_experimental_option('mobileEmulation', {
            'deviceName': 'iPhone 12'
        })
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()
    
    @pytest.mark.smoke
    def test_homepage_loads_mobile(self, mobile_driver):
        mobile_driver.get('http://localhost:3000')
        status = mobile_driver.find_element(By.CLASS_NAME, 'status')
        assert status is not None
```

### Option 2: Native Mobile App Testing (Future)

For a production mobile app (iOS/Android with React Native/Flutter):

**Setup**:

```bash
pip install appium-python-client
adb start-server  # For Android
```

**Test Example**:

```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

@pytest.mark.mobile
class TestMobileApp:
    @pytest.fixture
    def driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'app': '/path/to/app.apk',
            'automationName': 'UiAutomator2',
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        yield driver
        driver.quit()
    
    @pytest.mark.smoke
    def test_login_flow(self, driver):
        email_field = driver.find_element(AppiumBy.ID, 'com.example:id/email')
        email_field.send_keys('test@example.com')
        
        password_field = driver.find_element(AppiumBy.ID, 'com.example:id/password')
        password_field.send_keys('password123')
        
        login_button = driver.find_element(AppiumBy.ID, 'com.example:id/login')
        login_button.click()
        
        # Verify successful login
        welcome_msg = driver.find_element(AppiumBy.ID, 'com.example:id/welcome')
        assert 'Welcome' in welcome_msg.text
```

## Devices & Emulators

### Android

```bash
# List available devices
adb devices

# Create emulator
emulator -avd pixel_5_api_30

# Install app on emulator
adb install app.apk
```

### iOS

```bash
# Start simulator
xcode-select --install
simctl list devices

# Start specific simulator
open /Applications/Xcode.app/Contents/Developer/Applications/Simulator.app
```

## Test Pyramid for Mobile

```
        E2E (UI Flows)           20-30%
       /              \
      /  Integration   \        30-40%
     /   (API Mocking)  \
    /____________________\      40-50%
   /    Unit Tests      \
```

## Recommended Test Cases

### User Authentication
- Login with valid credentials
- Login with invalid credentials
- Logout
- Password reset

### Task Management
- Create task
- Edit task
- Mark as complete
- Delete task
- List user tasks

### Edge Cases
- Offline mode behavior
- Network interruption recovery
- Touch gestures (swipe, tap, long-press)
- Screen orientation changes
- Memory/performance under load

## Tools Comparison

| Tool | Use Case | Platform | Cost |
|------|----------|----------|------|
| **Appium** | Cross-platform (iOS/Android) | Native/Hybrid | Free (Open Source) |
| **Playwright** | Web + Mobile Web | Chromium, Firefox, WebKit | Free (Open Source) |
| **Selenium Grid** | Distributed mobile testing | Multiple devices | Free (Open Source) |
| **BrowserStack** | Cloud-based testing | 1000+ devices | Paid |
| **Sauce Labs** | Enterprise testing | Real devices | Paid |

## CI/CD Integration

### Local Testing

```bash
# Mobile tests
pytest -m mobile -v

# Specific device
pytest -m mobile -v --device=iphone_12
```

### Cloud Testing (BrowserStack)

```python
from appium import webdriver

def setup_browserstack_driver():
    caps = {
        'app': 'bs://your-app-id',
        'device': 'iPhone 12',
        'os_version': '15',
        'real_mobile': True,
    }
    return webdriver.Remote(
        'http://YOUR_USERNAME:YOUR_ACCESS_KEY@hub.browserstack.com/wd/hub',
        caps
    )
```

## Performance Metrics

Capture mobile-specific metrics:

```python
import time
from appium import webdriver

def test_app_startup_time():
    start = time.time()
    driver = webdriver.Remote(...)
    elapsed = time.time() - start
    
    assert elapsed < 5, f"App took {elapsed}s to start"

def test_scroll_performance():
    driver.execute_script('mobile: performanceLog', {'logType': 'syslog'})
    # Measure FPS during scroll
    logs = driver.get_log('performance')
    fps = analyze_fps(logs)
    assert fps >= 60, f"FPS dropped to {fps}"
```

## Best Practices

✅ **DO**:
- Test on real devices (not just emulators)
- Test on multiple OS versions
- Simulate network conditions
- Test touch interactions
- Monitor performance metrics
- Use explicit waits for mobile elements

❌ **DON'T**:
- Hard-code waits with sleep()
- Assume same behavior as web
- Ignore performance metrics
- Test only in portrait mode
- Skip network failure scenarios

## Future Implementation

To add mobile testing to this project:

1. Create mobile app (React Native/Flutter)
2. Add Appium configuration
3. Implement mobile test suite (tests/mobile/)
4. Integrate with CI/CD pipeline
5. Set up cloud device farm (BrowserStack/Sauce Labs)
6. Monitor mobile metrics in Allure reports

## Resources

- [Appium Documentation](http://appium.io/docs/)
- [Selenium Documentation](https://selenium.dev/)
- [Playwright Mobile Testing](https://playwright.dev/docs/mobile-testing)
- [BrowserStack Appium Testing](https://www.browserstack.com/docs/appium)
