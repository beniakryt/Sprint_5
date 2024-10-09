import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Завершение работы драйвера
    driver.quit()