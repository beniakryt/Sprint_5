import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestLogin:
    @pytest.mark.parametrize("email, password", [
        ('yurii142323223@yandex.ru', '123456'),  # Укажите ваш email и пароль
    ])
    def test_login_from_main_page(self, driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()

        driver.find_element(By.XPATH, EMAIL_FIELD_LK_XPATH).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_LK_XPATH).click()
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize("email, password", [
        ('yurii142323223@yandex.ru', '123456'),
    ])
    def test_login_from_personal_account(self, driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()

        driver.find_element(By.XPATH, EMAIL_FIELD_LK_XPATH).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_LK_XPATH).click()
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize("email, password", [
        ('yurii142323223@yandex.ru', '123456'),  # Укажите ваш email и пароль
    ])
    def test_login_via_registration_form(self, driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        driver.find_element(By.XPATH, REGISTRATION_LINK_XPATH).click()
        driver.find_element(By.XPATH, LOGIN_LINK_LK).click()
        driver.find_element(By.XPATH, EMAIL_FIELD_LK_XPATH).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_LK_XPATH).click()
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    @pytest.mark.parametrize("email, password", [
        ('yurii142323223@yandex.ru', '123456'),
    ])
    def test_login_via_password_recovery_form(self, driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        driver.find_element(By.XPATH, PASSWORD_RECOVERY_LINK_XPATH).click()

        driver.find_element(By.XPATH, LOGIN_LINK_LK).click()
        driver.find_element(By.XPATH, EMAIL_FIELD_LK_XPATH).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_FIELD_XPATH).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_LK_XPATH).click()
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

