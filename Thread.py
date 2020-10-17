from threading import *
import time
def add(a,b):
	print(a+b)
time.sleep(10)
t=Thread(target=add,args=(10,20))
t.start()
