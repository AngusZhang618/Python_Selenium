#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities   #（1）
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)     #（2）
#browser = webdriver.DesiredCapabilities.HTMLUNIT() # Get local session of firefox
browser.get("https://www.yahoo.com") # Load page
assert "Yahoo" in browser.title
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//*[@id='web']/ol/li[1]/div/div[1]/h3/a")
    print("ok")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()
