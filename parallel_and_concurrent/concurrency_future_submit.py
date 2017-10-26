#!/usr/bin/python3

from concurrent import futures

def pow2(n):
   return n * n

before = list(range(1000))
with futures.ThreadPoolExecutor(max_workers=4) as executor:

   print("submission starts")
   to_do = []
   for num in before:
      future = executor.submit(pow2, num)
      to_do.append(future)
   print("submission ends")

   after = []
   for future in futures.as_completed(to_do):
      res = future.result()
      after.append(res)

print(before[:5])
print(after[:5])
