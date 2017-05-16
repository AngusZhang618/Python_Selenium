#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import email

#the path of the email saved
PATH = ''

#Read file
def read_mail(path):
    if os.path.exists(path):
        with open(path) as fp:
            for line in fp:
                print(line)
    else:
        not_find_file()

#Open a file
def open_file(path):
    if os.path.exists(path):
        return open(path,'r')
    else:
        not_find_file()

#Create message
def get_message(path):
    if os.path.exists(path):
        fp = open_file(path)
        return email.message_from_file(fp)

    else:
        not_find_file()

#Get subject
def get_subject(path):
    if os.path.exists(path):
        message = get_message(path)
        print(type(message))
        return message.get("subject")
    else:
        not_find_file()

#解析subject对象
def parse_subject(msg):
    if msg != None:
        subject = msg.get('subject')
    else:
        empty_obj()

#获取发件人信息
def get_from(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get("from"))[1]
    else:
        empty_obj()

#获取发件人信息
def get_to(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get("to"))[1]
    else:
        empty_obj()

#获取邮件生成时间
def get_date(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get("date"))[1]
    else:
        empty_obj()

#获取邮件生成版本
def get_mime_version(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('mime-version'))[1]
    else:
        empty_obj()

#获取邮件文本类型
def get_content_type(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('contect-type'))[1]
    else:
        empty_obj()

#获取邮件ID
def get_message_id(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('message-id'))[1]
    else:
        empty_obj()

#文件不存在
def not_find_file():
    print("file not exists!")

#msg is empty
def empty_obj():
        print("msg is empty!")

def main():
    global PATH
    PATH = 'E:\WorkSpace\HelloWorld1.eml'
    print(PATH)
    msg = get_message(PATH)
    # print(msg)
    print('#' * 50)
    print('subject:{}'.format(get_subject(PATH)))
    print('#' * 50)
    print(parse_subject(msg))
    print('#' * 50)
    print('from:{}'.format(get_from(msg)))
    print('to:{}'.format(get_to(msg)))
    print('date:{}'.format(get_date(msg)))
    print('mime-version:{}'.format(get_mime_version(msg)))
    print('content-type:{}'.format(get_content_type(msg)))
    print('message-id:{}'.format(get_message_id(msg)))

if __name__ == '__main__':
    main()