from threading import *
class Test:
	def display(self):
		for i in range(10):
			print('Child Thread-2')
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
	print('Main Thread-2')
	
# C:\Users\Raj Muni\Desktop>py test.py
# Child Thread-2
# Main Thread-2
# Main Thread-2
# Child Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Main Thread-2
# Child Thread-2
# Main Thread-2
# Main Thread-2