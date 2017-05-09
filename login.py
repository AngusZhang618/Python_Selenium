#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from selenium import webdriver
import time
import unittest

class WebTest(unittest.TestCase):
    def setUp(self):
        u"""初始化"""
        self.driver = webdriver.Firefox()

    def login(self,username,passwd):
        u"""登录方法，账号密码参数化"""
        driver = self.driver
        driver.get("http://www.hordehome.com")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='ember804']//button[.='登录']").click()
        driver.find_element_by_id("login-account-name").send_keys(username)
        driver.find_element_by_xpath(".//*[@id='login-account-password']").clear()
        driver.find_element_by_xpath(".//*[@id='login-account-password']").send_keys(passwd)
        driver.find_element_by_xpath("//div[@class='modal-footer']/button[1]").click()

    def logout(self):
        u"""退出方法"""
        # driver = self.driver
        self.driver.find_element_by_xpath("//li[@id='current-user']/a/div/img").click()
        self.driver.find_element_by_xpath("//ul[@class='menu-links']//a[.=' 登出']").click()
        #检查是否正确退出

    def is_login_success(self):
        u"""判断是否登录成功"""
        try:
            time.sleep(10)
            text = self.driver.find_element_by_xpath(".//*[@id='current-user']/a/div/img").get_attribute("title")
            print(u"登录成功！")
            print(u"当前登录用户：",text)
            return True
        except Exception as e:
            print(u"登录失败！")
            print(e)
            return False

    def tearDown(self):
        self.driver.quit()

    def test01(self):
        print("Current Run:test01")
        self.login("hello","world")
        result = self.is_login_success()
        self.assertTrue(result)
    def test02(self):
        print("Current Run:test02")
        self.login("Angus","xxxxxx")
        result = self.is_login_success()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
