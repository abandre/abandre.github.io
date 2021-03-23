import random, time
from threading import BoundedSemaphore, Thread

max_itens = 5

#container = 0 
container = BoundedSemaphore(max_itens)

def producer(qtd):
    global container

    for i in range(qtd):
        time.sleep(0)        
        #container+=1
        container.release()

        print("[Producer]",time.ctime(),container)
        
        # try:
        #     container.release()
        #     print("Produced an item.")
        # except ValueError:
        #     print("Full, skipping.")

def consumer(qtd):
    global container

    for i in range(qtd):
        time.sleep(0)        
        #container-=1
        container.acquire()

        print("[Consumer]",time.ctime(),container)

        # if container.acquire(False):
        #     print("Consumed an item.")
        # else:
        #     print("Empty, skipping.")


if __name__=="__main__":     
    start = time.time() 

    qtd = random.randrange(3, 10)
    print(qtd)

    thread1 = Thread(target=producer,args=(qtd,))
    thread1.start()

    thread2 = Thread(target=consumer,args=(qtd,))
    thread2.start()

    thread1.join()
    thread2.join()

    print(container)

    end = time.time() 
    print('Time taken in seconds -', end - start)    
