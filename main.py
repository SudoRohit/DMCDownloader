import csv
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
driver.get("SITE/Webportal/Documents")

wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="DMC"]/div[1]'))).click()

data = []

with open('data/status.csv', 'r') as status:
    sta = csv.reader(status)
    for row in sta:
        data.append(row[0])

with open('data/status.csv', 'a') as addition:
    add = csv.writer(addition)

    with open('data/data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:

            if line[0] not in data:
                download = driver.find_element(By.XPATH, line[1])
                time.sleep(2)
                download.click()
                add.writerow([line[0]])
                time.sleep(5)