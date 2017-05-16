#!/usr/bin/env python
#-*- coding: UTF-8 -*-
l = ["1","2","3"]
m = ["1","2","3","4","5"]
a = set(m).difference(set(l))
print(a)
b = list(a)
b.sort()
print(b)