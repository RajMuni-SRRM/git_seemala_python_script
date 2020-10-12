from threading import *
def add(a,b):
	print(a+b)
	
t=Thread(target=add,args=(10,20))
t.start()
