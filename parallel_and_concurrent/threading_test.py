#!/usr/bin/python3

import threading
import time

class MyThread(threading.Thread):
   def __init__(self, name, sleep_time):
      threading.Thread.__init__(self)
      self.name = name
      self.sleep_time = sleep_time
   def run(self):
      print ("Starting " + self.name)
      time.sleep(self.sleep_time)
      print ("Exiting " + self.name)

thread_num = 3
threads = []
for i in range(thread_num):
    threads.append(MyThread("Thread-{}".format(i), 5 - i))

for th in threads:
    th.start()

for th in threads:
    th.join()

print("end")
