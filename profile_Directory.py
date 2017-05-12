#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver

#定义profile路径
profile_directory = r"C:\Users\Angus\AppData\Roaming\Mozilla\Firefox\Profiles\x8kc34k2.default"
#加载配置
profile = webdriver.FirefoxProfile(profile_directory)
#带配置启动浏览器
driver = webdriver.Firefox(profile)
driver.get("http://www.baidu.com")