#!/usr/bin/python3

import multiprocessing

def pow2(n):
   return n * n

before = list(range(100000000))
with multiprocessing.Pool(4) as p:
   after = p.map(pow2, before)

print(before[:5])
print(after[:5])
