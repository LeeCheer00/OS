#!/usr/bin/env python
# coding=utf-8
import multiprocesssing as mp


value = mp.Value('d', 1)
array = mp.Array('i', [1,3,4])

# 共享内存，cpu， 定义共享内存， 其他方法是不能交流的。
