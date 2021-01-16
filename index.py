from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from zones import tabs

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
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')))
# tab = driver.find_element_by_xpath('//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')
# tab.click()

# count the number of zips 
# how to count the number of zips in each section 
# zipcode = driver.find_elements_by_xpath('//*[@id="city_5"]/div/div/div/div/table/tbody/tr')
# print(len(zipcode))

# BROOKLYN
# for zone in tabs["brooklyn"]:
#     for index, code in enumerate(zone):
#         count = driver.find_element_by_xpath('//*[@id="city_1"]/div/div[1]/div/div/table/tbody/tr'.format(
#             region = 1, 
#             zone = 1
#         ))

# for index, zone in enumerate(tabs["bklyn"].keys()):
#     count = len(driver.find_elements_by_xpath('//*[@id="city_1"]/div/div[{index}]/div/div/table/tbody/tr'.format(index=index+1)))
#     print("{zone}: {count}".format(zone=zone, count=count))

# count number of zips 
for region_i, region in enumerate(tabs.keys()):
    print("\n{}".format(region))
    
    # switch tab 
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section/section/div/section/div[1]/ul/li[{region_i}]/a'.format(region_i=region_i+1))))
    tab = driver.find_element_by_xpath('//*[@id="content"]/section/section/div/section/div[1]/ul/li[{region_i}]/a'.format(region_i=region_i+1))
    tab.click()

    # count 
    for zone_i, zone in enumerate(tabs[region].keys()):
        if (len(region) > 1):
            count = len(driver.find_elements_by_xpath('//*[@id="city_{region_i}"]/div/div[{zone_i}]/div/div/table/tbody/tr'.format(
                zone_i=zone_i+1,
                region_i=region_i+1
            )))
        else:
            count = len(driver.find_elements_by_xpath('//*[@id="city_{region_i}"]/div/div/div/div/table/tbody/tr'.format(
                region_i=region_i+1
            )))
        print("{zone}: {count}".format(zone=zone, count=count))
