import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestConstructorSections:

    def test_constructor_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ACTIVE_BUNS_TAB_XPATH))
        )

        active_tab_text = driver.find_element(By.XPATH, ACTIVE_BUNS_TAB_XPATH).text
        assert active_tab_text == "Булки"

    def test_constructor_sauces_section(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(By.XPATH, SAUCES_TAB_XPATH).click()

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ACTIVE_SAUCES_TAB_XPATH))
        )

        active_tab_text = driver.find_element(By.XPATH, ACTIVE_SAUCES_TAB_XPATH).text
        assert active_tab_text == "Соусы"

    def test_constructor_fillings_section(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(By.XPATH, FILLINGS_TAB_XPATH).click()

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ACTIVE_FILLINGS_TAB_XPATH))
        )

        active_tab_text = driver.find_element(By.XPATH, ACTIVE_FILLINGS_TAB_XPATH).text
        assert active_tab_text == "Начинки"
