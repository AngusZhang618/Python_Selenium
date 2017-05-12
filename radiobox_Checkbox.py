#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

profile_directory = r"C:\Users\Angus\AppData\Roaming\Mozilla\Firefox\Profiles\x8kc34k2.default"
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
driver.get("http://localhost:63342/Workspace/Python_Selenium/2.html")
time.sleep(2)
driver.find_element_by_id("boy").click()
s = driver.find_element_by_id("boy").is_selected()
print(s)
time.sleep(2)
driver.find_element_by_id("girl").click()
s = driver.find_element_by_id("girl").is_selected()
print(s)
time.sleep(2)

# driver.find_element_by_id("c1").click()
# driver.find_element_by_id("c2").click()
c = driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in c:
    print(i,i.is_selected())
    if not i.is_selected():
        i.click()