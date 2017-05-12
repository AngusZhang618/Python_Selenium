#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.runoob.com/jsref/obj-window.html")
time.sleep(5)
#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(2)
#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
time.sleep(2)
#聚焦元素
target = driver.find_element_by_xpath(".//*[@id='content']/table[2]/tbody/tr[20]/td[1]/a")
driver.execute_script("arguments[0].scrollIntoView();",target)