from threading import *
l=RLock()
print('Current thread name is:',current_thread().name)
print('Main thread trying to acquire lock....')
l.acquire()
print('Main thread trying to acquire lock again...')
l.acquire()
print('Current thread name is:',current_thread().name ,'and is alive:',current_thread().isAlive())
print('Main thread acquire same lock again..')
print('Current thread name is:',current_thread().name ,'and is alive:',current_thread().isAlive())



# C:\Users\Raj Muni\Desktop>py test.py
# Current thread name is: MainThread
# Main thread trying to acquire lock....
# Main thread trying to acquire lock again...
# Current thread name is: MainThread and is alive: True
# Main thread acquire same lock again..
# Current thread name is: MainThread and is alive: True