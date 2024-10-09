import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from helpers import generate_unique_email

class TestStellarBurgers:
    @pytest.mark.parametrize("name, email, password", [
        ('Иван', generate_unique_email(), '123456'),
    ])
    def test_successful_registration(self, driver, name, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        driver.find_element(By.XPATH, REGISTRATION_LINK_XPATH).click()
        driver.find_element(By.XPATH, NAME_FIELD_XPATH).send_keys(name)
        driver.find_element(By.XPATH, EMAIL_FIELD_XPATH).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, SUBMIT_REGISTRATION_BUTTON_XPATH).click()

        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_with_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        driver.find_element(By.XPATH, REGISTRATION_LINK_XPATH).click()
        driver.find_element(By.XPATH, NAME_FIELD_XPATH).send_keys('Yurii')
        driver.find_element(By.XPATH, EMAIL_FIELD_XPATH).send_keys(generate_unique_email())
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys('123')  # Некорректный пароль
        driver.find_element(By.XPATH, SUBMIT_REGISTRATION_BUTTON_XPATH).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, ERRORPASSWORD_MESSAGE_XPATH)))

        error_message = driver.find_element(By.XPATH, ERRORPASSWORD_MESSAGE_XPATH).text
        assert "Некорректный пароль" in error_message

