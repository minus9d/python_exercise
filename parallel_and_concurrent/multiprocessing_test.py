#!/usr/bin/python3

import multiprocessing
import time

class MyProcess(multiprocessing.Process):
   def __init__(self, name, sleep_time):
      multiprocessing.Process.__init__(self)
      self.name = name
      self.sleep_time = sleep_time
   def run(self):
      print ("Starting " + self.name)
      time.sleep(self.sleep_time)
      print ("Exiting " + self.name)

process_num = 3
processs = []
for i in range(process_num):
    processs.append(MyProcess("Process-{}".format(i), 5 - i))

for th in processs:
    th.start()

for th in processs:
    th.join()

print("end")
