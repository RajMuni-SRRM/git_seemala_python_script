from threading import *
def display():
	print('This code (display function) executed by thread:',current_thread().getName())
t=Thread(target=display)
t.start()
print('This code executed by Thread:',current_thread().getName())


# C:\Users\Raj Muni\Desktop>py test.py
# This code (display function) executed by thread: Thread-1
# This code executed by Thread: MainThread