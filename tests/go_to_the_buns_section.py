from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()

assert driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]")

driver.quit()
