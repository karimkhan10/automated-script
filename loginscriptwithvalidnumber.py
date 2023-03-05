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

driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/form/div[1]/div/div[1]/input').send_keys('03172955361')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/form/div[2]/div/button').click()
time.sleep(20)

# Enter OTP manually because Of build restriction

