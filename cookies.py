#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com/")
# driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
cookies = driver.get_cookies()
print(len(cookies))
for i in cookies:
    print("%s------>%s"%(i['name'],i['value']))


driver.quit()