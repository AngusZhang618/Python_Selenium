#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import time
from selenium import webdriver

class AutoLogin():
    def setUp(self):
        self.driver = webdriver.Firefox()

    def getAuthCode(self,imagePara):
        if os.path.exists(imagePara):
            cmd = r'tesseract.exe '
            command = cmd + imagePara + ' code'
            os.system(command)
            file = open('code.txt')
            code = file.read()
            return code
            file.close()
        else:
            print("No image under this folder")
            return False

    def login(self, username, passwd):
        u"""登录方法，账号密码参数化"""
        driver = self.driver
        path = ''
        driver.get(path)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("").click()
        driver.find_element_by_id("").send_keys(username)
        driver.find_element_by_xpath("").clear()
        driver.find_element_by_xpath("").send_keys(passwd)
        driver.find_element_by_xpath("").click()

    def readText(self):
        path = ''
        file = open(path)
        lines = file.readlines()
        account = []
        for i in lines:
            l = i.strip().split('|')
            account.append(l)
        return account
        file.close()

    def is_login_success(self):
        u"""判断是否登录成功"""
        try:
            time.sleep(10)
            text = self.driver.find_element_by_xpath("").get_attribute("title")
            print(u"登录成功！")
            print(u"当前登录用户：",text)
            return True
        except Exception as e:
            print(u"登录失败！")
            print(e)
            return False