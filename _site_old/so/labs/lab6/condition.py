import random
import threading
import time

fila = []
resultado = []

condition = threading.Condition()

def Consumidor():
    global fila, resultado

    while True:
        try:            
            if len(fila)<2:
                condition.acquire()
                condition.notifyAll()
                condition.release()

            x = fila.pop(0)
            print('\nCONSUMIDOR: processando tarefa',x)
            time.sleep(2)
            resultado.append(x)
        except:
            print("aqui")
            time.sleep(2)
            if len(fila) == 0:
                break
  
def Produtor():
    global fila, resultado
       
    for i in range(10):
        if len(fila)<2:
            condition.acquire()
            condition.notify()
            condition.release()

        condition.acquire()
        condition.wait()
        condition.release()

        fila.append(i)
        tempo=random.random()
        time.sleep(tempo)
        print("\nPRODUTOR:",tempo)
        print('PRODUTOR: tarefas pendentes:',len(fila),fila)

    while True:
        print('PRODUTOR: tarefas terminadas:',len(resultado),resultado)
        if len(fila) == 0:
           break
        time.sleep(1)
   
def Produtor2():
    global fila, resultado
       
    for i in range(11,20):
        if len(fila)<2:
            condition.acquire()
            condition.notify()
            condition.release()

        condition.acquire()
        condition.wait()
        condition.release()

        fila.append(i)
        tempo=random.random()
        time.sleep(tempo)
        print("\nPRODUTOR2:",tempo)
        print('PRODUTOR2: tarefas pendentes:',len(fila),fila)

    while True:
        print('PRODUTOR2: tarefas terminadas:',len(resultado),resultado)
        if len(fila) == 0:
           break
        time.sleep(1)

if __name__=="__main__": 
    start = time.time() 
       
    t1 = threading.Thread(target=Consumidor)
    t2 = threading.Thread(target=Produtor)
    t3 = threading.Thread(target=Produtor2)    

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time.time() 
    print('Time taken in seconds -', end - start)    
