from threading import *
import time
l=Lock()
def wish(name):
	l.acquire()
	for i in range(10):
		print('Good Evening:',end='')
		time.sleep(2)
		print(name)
	l.release()
t1=Thread(target=wish,args=(input('enter the first thread args:'),))
t2=Thread(target=wish,args=(input('enter the first thread args:'),))
t1.start()
t2.start()



# C:\Users\Raj Muni\Desktop>py test.py
# enter the first thread args:rajmuni
# enter the first thread args:seemala
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:rajmuni
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala
# Good Evening:seemala