from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 20)

driver.get('SITE/login')

userid = driver.find_element(By.ID, 'username')
userid.send_keys('USERID')

password = driver.find_element(By.ID, 'password')
password.send_keys('PASSWORD')

signin = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[2]/div/form/button')
signin.click()

wait.until(ec.title_is("Home Page"))
driver.get("SITE/Documents")

wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="DMC"]/div[1]'))).click()

download = driver.find_elements(By.XPATH, "//div[@id='DMC-content']//div//div//div//div[1]//div[1]//div[1]//div[2]//span[2]//*[name()='svg']")
time.sleep(1)

for i in download:
    i.click()
    time.sleep(5)