#!/usr/bin/env python
#-*- coding: UTF-8 -*-
l = [1,2,3,4,5]
m = [1,2,3,4]

n = [lambda x :  x in l and x not in m]
for i in n:
    print(i)

help(set(l).isdisjoint(set(m)))

