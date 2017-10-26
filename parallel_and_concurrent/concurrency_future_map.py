#!/usr/bin/python3

from concurrent import futures
import itertools

def pow2(n):
   return n * n

before = list(range(10000))
with futures.ProcessPoolExecutor(max_workers=4) as executor:
   after = executor.map(pow2, before)
print("map done")

print(before[:5])
print(list(itertools.islice(after, 5))) # iterableの最初の5個を表示
