# -*- coding: utf-8 -*-

import poplib
import email
from email import parser
import string

host = 'pop.qq.com'
username = '275764611'
password = 'nphmypjzmzllbhjf'

pop_conn = poplib.POP3_SSL(host)
pop_conn.user(username)
pop_conn.pass_(password)

#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
# Concat message pieces:
# messages = ["\n".join(mssg[1]) for mssg in messages]
mail = []
for mssg in messages:
    print('*'*50)
    print(messages.index(mssg))
    for imssg in mssg[1]:
        # print(type(imssg))
        # imssg.decode('unicode_escape')
        # messages.append("\n".join(imssg))
        print(imssg.decode())
        mail.append(imssg)
    print(messages.index(mssg))
    print("*"*50)
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