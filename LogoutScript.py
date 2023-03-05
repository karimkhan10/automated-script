from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import random
from selenium.webdriver.support.ui import Select

# Create driver objcet

s = Service("C:\\Users\AbdulKarim\\OneDrive - DataQ Health\\Desktop\\chromeDriver\\chromeDriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://web.udhaar.pk/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="startUdhaar"]').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys('03012469348')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/form/div[2]/div/button').click()
time.sleep(30)

# Enter OTP manually because Of build restriction

driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/nav/button').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/nav/div[7]').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button[2]/span[1]').click()
time.sleep(10)



