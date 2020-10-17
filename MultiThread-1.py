from threading import *
def display():
	for i in range(10):
		print('child thread')
t=Thread(target=display)
t.start()
for i in range(10):
	print('Main Thread')
	

# C:\Users\Raj Muni\Desktop>py test.py
# child thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# Main Thread
# child thread
# child thread
# child thread
# child thread
# child thread
# child thread
# child thread
# child thread
# child thread

# C:\Users\Raj Muni\Desktop>py test.py
# child thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# child thread
# Main Thread
# child thread