from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

WebDriverWait(driver, 3).until(EC.url_contains("/login"))

driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a').click()

WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

driver.quit()
