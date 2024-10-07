from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('yuriibeniashevskyi14399@yandex.ru')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('Qwerty23')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

driver.quit()
