#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath(".//*[@id='kw']").clear()
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
driver.find_element_by_xpath(".//*[@id='kw']").submit()
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("kw").submit()
time.sleep(10)
s = driver.find_elements_by_css_selector("h3.t>a")
print(len(s))
for i in s:
    print(i.get_attribute("href"))

