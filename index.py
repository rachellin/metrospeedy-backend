from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import pprint
from csv_ops import write_data
from zones import *

from settings import BACKEND_LINK, USERNAME, PASSWORD, ZIPS_LINK

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://{}".format(BACKEND_LINK))

# wait for page to full load
time.sleep(1)

# login
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_xpath('//*[@id="login-box"]/button')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.click()

# navigate to managment console
driver.get("https://{}".format(ZIPS_LINK))

# switch tab
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')))
# tab = driver.find_element_by_xpath('//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')
# tab.click()

# count the number of zips 
# how to count the number of zips in each section 
# zipcode = driver.find_elements_by_xpath('//*[@id="city_5"]/div/div/div/div/table/tbody/tr')
# print(len(zipcode))

# for index, zone in enumerate(tabs["bklyn"].keys()):
#     count = len(driver.find_elements_by_xpath('//*[@id="city_1"]/div/div[{index}]/div/div/table/tbody/tr'.format(index=index+1)))
#     print("{zone}: {count}".format(zone=zone, count=count))

# count number of zips 
def count_zips ():
    '''print the number of zips for each set in each region'''
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
            zips_are_equal(region, region_i, zone, zone_i, count)
            write_data("zip_check_2.csv", fieldnames, zip_check_data)
            #print("{zone}: {count}".format(zone=zone, count=count))

def zips_are_equal (region, region_i, zone, zone_i, count):
    added_zips = []
    for x in range(count):
        if (len(region) > 1):
            zip_code = driver.find_element_by_xpath('//*[@id="city_{region_i}"]/div/div[{zone_i}]/div/div/table/tbody/tr[{x}]/td[1]'.format(
                x = x+1,
                zone_i = zone_i+1,
                region_i = region_i+1
            )).text
        else:
            zip_code = driver.find_element_by_xpath('//*[@id="city_{region_i}"]/div/div/div/div/table/tbody/tr[{x}]/td[1]'.format(
                x = x+1,
                region_i = region_i+1
            )).text
        if (zip_code != "420 E 82ND ST, 10028"): # temp
            added_zips.append(zip_code)
    added_zips = [int(i) for i in added_zips] # convert list items to integers
    equal = set(added_zips) == set(tabs[region][zone])
    print(zone, ": ", equal)
    # add data to list of dictionaries 
    zip_check_data.append(
        {
            "zone": zone,
            "equal": equal,
            "diff1": list(set(tabs[region][zone]) - set(added_zips)),
            "diff2": list(set(added_zips) - set(tabs[region][zone]))
        }
    )   

#count_zips()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')))
# tab = driver.find_element_by_xpath('//*[@id="content"]/section/section/div/section/div[1]/ul/li[1]/a')
# count = len(driver.find_elements_by_xpath('//*[@id="city_1"]/div/div[1]/div/div/table/tbody/tr'))
# arr = []
# for x in range(count):
#     zip_code = driver.find_element_by_xpath('//*[@id="city_1"]/div/div[1]/div/div/table/tbody/tr[{x}]/td[1]'.format(x=x+1)).text
#     arr.append(zip_code)
# arr = [int(i) for i in arr] # convert list items to integers
# print(set(arr) == set(tabs["bklyn"]["north"]))


