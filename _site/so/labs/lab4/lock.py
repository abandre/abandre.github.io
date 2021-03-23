from threading import Thread
from threading import Lock
import time
import random

g = 0
lock = Lock()

def incrementa():
	global g

	lock.acquire()
	tmp = g     # le valor
	tmp += 1    # incrementa
	time.sleep(random.randrange(0, 2))
	g = tmp     # escreve
	lock.release()

if __name__=="__main__": 
	start = time.time() 

	thread1 = Thread(target=incrementa)
	thread1.start()

	thread2 = Thread(target=incrementa)
	thread2.start()

	thread1.join()
	thread2.join()

	print(g)

	end = time.time() 
	print('Time taken in seconds -', end - start)    