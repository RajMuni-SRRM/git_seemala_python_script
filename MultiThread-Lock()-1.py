from threading import *
import time
l=RLock()
def wish(name):
	l.acquire()
	for i in range(5):
		print('Good Evening:',end='')
		time.sleep(2)
		print(name)
	l.release()
t1=Thread(target=wish,args=(input('enter the first thread args:'),))
t2=Thread(target=wish,args=(input('enter the second thread args:'),))
# t3=Thread(target=wish,args=(input('enter the third thread args:'),))
# t4=Thread(target=wish,args=(input('enter the fourth thread args:'),))
t1.start()
t2.start()
# t3.start()
# t4.start()


