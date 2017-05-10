#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Firefox()
dr.get("http://www.baidu.com")
mouse = dr.find_element_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(dr).move_to_element(mouse).perform()
dr.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
time.sleep(15)
s = dr.find_element_by_xpath(".//*[@id='nr']")
#通过value的值选择
Select(s).select_by_value("20")
time.sleep(2)
#通过index选择
Select(s).select_by_index(2)
time.sleep(2)
#通过text选择
Select(s).select_by_visible_text("每页显示10条")
#打印所有的option---非已选择的选项
all_s = Select(s).options
for i in all_s:
    print(i.text)