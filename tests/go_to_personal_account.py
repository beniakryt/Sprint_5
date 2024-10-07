from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)

driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON_XPATH).click()

WebDriverWait(driver, 3).until(EC.url_contains("/login"))

assert "https://stellarburgers.nomoreparties.site/login" in driver.current_url

driver.quit()
