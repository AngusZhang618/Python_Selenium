#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading
from time import ctime,sleep

loops = [4,2]

class MyThread(threading.Thread):

    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self._args = args
        self.name = name

    def run(self):
        self.func(*self._args)


def loop(nloop,nsec):
    print("Start loop",nloop,"at",ctime())
    sleep(nsec)
    print("End loop",nloop,"at",ctime())


def main():
    print("Start at",ctime())
    threads = []
    nloop = range(len(loops))

    for i in nloop:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

    print("End at",ctime())

if __name__ == '__main__':
    main()
