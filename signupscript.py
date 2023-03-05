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
driver.get("https://www.hubspot.com/")
driver.maximize_window()
time.sleep(2)

# Find the "accept cookies" button and click on it
try:
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[1]').click()
except NoSuchElementException:
    # If the "accept cookies" button is not found, ignore the error and continue
    pass
driver.find_element(By.XPATH, '//*[@id="burger-submenu"]/ul[2]/li/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="hs_cos_wrapper_module_164794466131010"]/section/div/div/div/div/a[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="UIFormControl-2"]').send_keys("New")
driver.find_element(By.XPATH, '//*[@id="UIFormControl-4"]').send_keys("User")

driver.find_element(By.XPATH, '//*[@id="UIFormControl-6"]').send_keys("opq654@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(1)


search_dropdown = driver.find_element(By.XPATH, '//*[@id="UIFormControl-8"]/div/div[1]/input')
search_dropdown.click()
search_dropdown.send_keys("info")
driver.find_element(By.XPATH, '//*[@id="react-select-2--option-0"]/span/span/button').click()
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[2]/button').click()
time.sleep(2)

job_dropdown = driver.find_element(By.XPATH, '//*[@id="UIFormControl-10"]/div/div[1]/input')
job_dropdown.click()
job_dropdown.send_keys("qa")
driver.find_element(By.XPATH, '//*[@id="react-select-3--option-0"]/span/span/button').click()
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="UIFormControl-12"]').send_keys('testing company')
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/div/div[2]/div/div/span/p').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="UIFormControl-31"]').send_keys('www.Mysite.com')
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/form/div[2]/button').click()
#add wait for manually enter the varification code which I receive through email
time.sleep(20)

driver.find_element(By.XPATH, '//*[@id="UIFormControl-27"]').send_keys('MyTest@321')
driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/div/form/div[2]/button').click()

driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div/div/div/div/div[3]/button').click()


