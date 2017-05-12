#!/usr/bin/env python
# -*- coding: UTF-8 -*-

path = 'E:\\WorkSpace\\1.txt'
file = open(path)
lines = file.readlines()
for i in lines:
    l = i.strip().split('|')
    user = l[0]
    pwd = l[1]
    print(l)

    # print("username:",user)
    # print("password:",pwd)