#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

url = "http://localhost:63342/Workspace/Python_Selenium/1.html"
dr = webdriver.Firefox()
dr.get(url)
time.sleep(2)
#找到alert并点击
dr.find_element_by_id("alert").click()
time.sleep(1)
#切换到alter
t = dr.switch_to.alert
#打印当前alert文本信息
print(t.text)
#相当于点击确认按钮
t.accept()
dr.find_element_by_id("confirm").click()
time.sleep(1)
t = dr.switch_to.alert
print(t.text)
t.accept()
#点击取消
# t.dismiss()
dr.find_element_by_id("prompt").click()
time.sleep(1)
t = dr.switch_to.alert
print(t.text)
#往prompt文本框输入文字
t.send_keys("Hello Selenium")
t.accept()