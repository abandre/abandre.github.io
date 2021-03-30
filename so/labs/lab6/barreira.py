from random import randrange
from threading import Barrier, Thread, current_thread
from time import ctime, sleep

b = Barrier(4)

def player():
    sleep(randrange(1, 6))
    print("%s reached the barrier at: %s" % (current_thread().name, ctime()))
    b.wait()
    
threads = []
print("Race starts now…")
for i in range(4):
    threads.append(Thread(target=player))
    threads[-1].start()

for thread in threads:
    thread.join()
print("Race over!")


#https://www.ppgia.pucpr.br/~jamhour/Pessoal/Graduacao/Ciencia/Python/SincProcessos.html

