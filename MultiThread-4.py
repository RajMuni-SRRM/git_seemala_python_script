import time
from threading import *
def wish(name):
	for i in range(10):
		print('Good evening:',end='')
		time.sleep(3)
		print(name)
t1=Thread(target=wish,args=('raj',))
time.sleep(3)
t2=Thread(target=wish,args=('muni',))
t1.start()
t2.start()


# C:\Users\Raj Muni\Desktop>py test.py
# Good evening:Good evening:muni
# raj
# Good evening:Good evening:muni
# raj
# Good evening:Good evening:raj
# muni
# Good evening:Good evening:muni
# raj
# Good evening:Good evening:raj
# muni
# Good evening:Good evening:muni
# raj
# Good evening:Good evening:muni
# raj
# Good evening:Good evening:raj
# muni
# Good evening:Good evening:raj
# muni
# Good evening:Good evening:muni
# raj