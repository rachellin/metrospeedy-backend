from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get('https://app.metrospeedy.com/employee/login/?next=/employee/')

# wait for page to full load
time.sleep(1)

# login
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_xpath('//*[@id="login-box"]/button')

username.send_keys("rachel@metrospeedy.com")
password.send_keys("bocajnats")
submit.click()

# navigate to managment console
driver.get("https://app.metrospeedy.com/employee/management/#/zipcodes")

# switch tab
tabs = ["bklyn", "man", "wc", "li", "si", "bronx", "queens"]
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section/section/div/section/div[1]/ul/li[5]/a')))
tab = driver.find_element_by_xpath('//*[@id="content"]/section/section/div/section/div[1]/ul/li[5]/a')
tab.click()

# count the number of zips 
# how to count the number of zips in each section 
zipcode = driver.find_elements_by_xpath('//*[@id="city_5"]/div/div/div/div/table/tbody/tr')
print(len(zipcode))
