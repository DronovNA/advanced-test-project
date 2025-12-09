# Мобильное Тестирование (Appium)

## Обзор

Текущая версия проекта сосредоточена на **API и бэкенд тестировании**.

Мобильное тестирование использует **Appium** для кросс-платформного тестирования iOS/Android нативных приложений.

## Рекомендуемые Категории Тестов

### Автентификация
- Вход с корректными credentials
- Вход с некорректными credentials
- Выход
- Сброс пароля

### Обычные Основные Операции
- Отключение сыти
- Покрытие сети в локальных тестах
- Ориентация экрана
- Перформанс девайса

## Настройка Appium

```bash
# Установка
npm install -g appium
npm install -g appium-inspector

# Настройка Android SDK
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Установка Python клиента
pip install appium-python-client
```

## Примеры Пытон Тестов

```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

@pytest.mark.mobile
@pytest.mark.smoke
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
    
    def test_app_launch(self, driver):
        assert driver.current_activity
    
    def test_login_mobile(self, driver):
        email = driver.find_element(AppiumBy.ID, 'com.app:id/email')
        email.send_keys('test@example.com')
        
        password = driver.find_element(AppiumBy.ID, 'com.app:id/password')
        password.send_keys('password')
        
        login_btn = driver.find_element(AppiumBy.ID, 'com.app:id/login')
        login_btn.click()
        
        # Проверка
        from appium.webdriver.support.ui import WebDriverWait
        from appium.webdriver.support import expected_conditions
        
        wait = WebDriverWait(driver, 10)
        welcome = wait.until(
            expected_conditions.presence_of_element_located(
                (AppiumBy.ID, 'com.app:id/welcome')
            )
        )
        assert welcome.is_displayed()
```

## Кортес Установки

```bash
# Построить апп
./gradlew assembleDebug  # Android
xcodebuild build          # iOS

# Установить на девайс
 adb install app.apk

# Расположение в CI/CD
pytest tests/mobile/ -v -m mobile
```
