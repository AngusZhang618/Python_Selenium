#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.hao123.com/")
time.sleep(10)
#获取当前窗口句柄
h = driver.current_window_handle
print(h,driver.title)
#获取链接
s = driver.find_elements_by_css_selector(".govsite-link.g-ib")
for i in range(len(s)):
    print(s[i].get_attribute("href"),s[i].text)
    s[i].click()

all_h = driver.window_handles
print(all_h,len(all_h))
for i in all_h:
    driver.switch_to.window(i)
    print(i,driver.title)
    time.sleep(2)