import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestProfileNavigation:

    def test_navigate_to_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()

        # Ожидаем, что URL изменится на личный кабинет
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Не удалось перейти на страницу личного кабинета"

    def test_navigate_from_profile_to_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()

        # Переход из личного кабинета в конструктор
        driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON_XPATH).click()

        # Ожидаем, что URL изменится на страницу конструктора
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', "Не удалось перейти на страницу конструктора"

    def test_navigate_from_profile_to_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, MAIN_LK_BUTTON).click()

        # Переход по клику на логотип Stellar Burgers
        driver.find_element(By.CSS_SELECTOR, LOGO_CSS).click()

        # Ожидаем, что URL изменится на главную страницу
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', "Не удалось перейти на главную страницу"
