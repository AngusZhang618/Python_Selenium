#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import time
from selenium import webdriver

class AutoLogin():


    def getAccount(self):
        filePath = 'D:\\WorkSpace\\Python_Selenium\\1.txt'
        file = open(filePath)
        lines = file.readlines()
        account = []
        for i in lines:
            l = i.strip().split('|')
            account.append(l)
        return account
        file.close()

    def findUser(self,user):
        account = self.getAccount()
        for i in account:
            if i[0].startswith(user):
                return i
        # return l


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


if __name__ == '__main__':
    auto = AutoLogin()
    authCodePath = 'D:\\WorkSpace\\Python_Selenium\\1.jpg'

    driver = webdriver.Firefox()
    path = 'https://www.walkiemate.com/hr_communication/login.jsp'
    driver.get(path)
    driver.implicitly_wait(10)

    account = auto.findUser("angus")
    print(account)
    username = account[0]
    passwd = account[1]
    driver.find_element_by_xpath(".//*[@id='username']").clear()
    driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    driver.find_element_by_xpath(".//*[@id='password']").clear()
    driver.find_element_by_xpath(".//*[@id='password']").send_keys(passwd)
    driver.find_element_by_xpath(".//*[@id='checkCode']").screenshot("1.jpg")
    authCode = auto.getAuthCode(authCodePath)
    #input the auth code
    driver.find_element_by_xpath(".//*[@id='checkValid']").clear()
    driver.find_element_by_xpath(".//*[@id='checkValid']").send_keys(authCode)
    driver.find_element_by_xpath(".//*[@id='login']/div[7]").click()
    driver.implicitly_wait(20)
    if driver.find_element_by_css_selector("#personImg").is_displayed():
        text = driver.find_element_by_xpath(".//*[@id='person_Div']/div/div[2]").get_attribute("innerHTML")
        print("当前登录用户：",text.strip())
    else:
        text = driver.find_element_by_xpath("html/body/div[3]/span").text
        print(text)
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='checkDivId']").click()
    driver.implicitly_wait(20)
    text = driver.find_element_by_xpath("html/body/div[11]/div[2]/div[1]").get_attribute("innerHTML")
    print(text)
    driver.quit()