from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import *

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)

driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Yurii')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('yuriibeniashevskyi14399@yandex.ru')

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123')

driver.find_element(By.XPATH, REGISTRATION_BUTTON_XPATH).click()
WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error")))

error_message = driver.find_element(By.CLASS_NAME, 'input__error').text
assert "Некорректный пароль" in error_message

driver.quit()
