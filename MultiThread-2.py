from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print('Child Thread Name',current_thread().getName())
t=MyThread()
t.setName('Rajmuni')
t.start()
for i in range(10):
	print('Main thread-1')
	

# C:\Users\Raj Muni\Desktop>py test.py
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Child Thread Name Rajmuni
# Child Thread Name Rajmuni
# Main thread-1
# Main thread-1
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1
# Child Thread Name Rajmuni
# Main thread-1