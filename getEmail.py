#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from imaplib import IMAP4
import email
s = IMAP4('imap.qq.com')
s.login('275764611@qq.com','nphmypjzmzllbhjf')
s.select('INBOX',True)
typ, data = s.search(None,'SEEN')
print(data)
t = 0
for num in (str(data[0])).split():
    rsp,data = s.fetch('1','(BODY[HEADER])')
    msg = email.message_from_string(str(data[0][1]))
    # print('subject:{}'.format(msg.get('subject')))
    print(msg.get('from'))
s.close()
s.logout()

