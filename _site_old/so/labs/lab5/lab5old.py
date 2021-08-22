import random, time
from threading import BoundedSemaphore, Thread

max_itens = 5
count=0
itens=[]

#container = 0 
#container = BoundedSemaphore(max_itens)

def producer(qtd):
    global count
    global itens

    for i in range(qtd):        
        item = random.randrange(1, 10)

        if count<max_itens:
            itens.append(item)
            time.sleep(1)        
            count+=1
            print("[Producer]",time.ctime(),item,itens,count)
        else:
            print("[Producer] - FULL")

        # try:
        #     container.release()
        #     print("Produced an item.")
        # except ValueError:
        #     print("Full, skipping.")

def consumer(qtd):
    global count
    global itens

    for i in range(qtd):        
        if count>0:
            item = itens.pop(count-1)
            time.sleep(1)        
            count-=1            
            print("[Consumer]",time.ctime(),item,itens,count)
        else:
            print("[Consumer] - EMPTY")

        # print("[Consumer]",time.ctime(),container)

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

    print(itens)
    print(count)

    end = time.time() 
    print('Time taken in seconds -', end - start)    
