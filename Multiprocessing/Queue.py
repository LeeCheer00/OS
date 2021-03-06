#!/usr/bin/env python
# coding=utf-8
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(10000):
        res += i+i**2+i**3
    q.put(res)# queue

def multcore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)

def normal():
    res = 0 
    for i in range(10000):
        res += i+i**2+i**3
if __name__ == '__main__':
    
