# -*- coding: utf-8 -*-

import poplib
import email
from email import parser
import string
from imaplib import IMAP4
import email
import os

username = '275764611'
password = 'nphmypjzmzllbhjf'
def getUnseenmail():
    s = IMAP4('imap.qq.com')
    s.login(username,password)
    s.select('INBOX',True)
    typ, data = s.search(None,'UNSEEN')
    print(data)
    s.close()
    s.logout()
    return data


host = 'pop.qq.com'

pop_conn = poplib.POP3_SSL(host)
pop_conn.user(username)
pop_conn.pass_(password)

#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:

unseenmail = getUnseenmail()
unseenmail = str(unseenmail[0].decode()).split(' ')
unseenmail = unseenmail[::-1]

print(unseenmail)
print(len(messages))
print(messages[13])
for i in unseenmail:
    lines = messages[int(i)-1][1]
    for i in lines:
        os.system('type > NUL > %d.eml'%int(i))
        path = os.getcwd() + "\\" + "%d.eml'%int(i)"
        print(path)
        file = open(path,'a')
        print('Open the file')
        file.write(lines)
        file.close()
        print('finished!')
        # print(type(imssg))
        # imssg.decode('unicode_escape')
        # messages.append("\n".join(imssg))
        # print(imssg.decode())
# print(messages)

#Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
i = 0
for index in range(0,len(messages)):
    message = messages[index];
    print(type(message))
    i = i + 1;
    subject = message.get('subject')
    print(type(subject))
    mailName = u"mail%d.%s" % (i, subject)
    print("Date: ", message["Date"])
    print("From: ", email.utils.parseaddr(message.get('from'))[1])
    print("To: ", email.utils.parseaddr(message.get('to'))[1])
    print("Subject: ", subject)
    print("Data: ")
pop_conn.quit()