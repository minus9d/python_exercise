#!/usr/bin/python3
# cf. http://dabeaz.blogspot.jp/2009/11/python-thread-deadlock-avoidance_20.html

import threading

a_lock = threading.Lock()
b_lock = threading.Lock()

def foo():
    with a_lock:
         with b_lock:
            print ("a -> b")

def bar():
    with b_lock:
         with a_lock:
            print ("b -> a")

class MyThread(threading.Thread):
   def __init__(self, func):
      threading.Thread.__init__(self)
      self.func = func
   def run(self):
      while True:
         self.func()

th1 = MyThread(foo)
th2 = MyThread(bar)

th1.start()
th2.start()

th1.join()
th2.join()
