import random
import threading
import time

fila = []
resultado = []

def Consumidor():
    global fila, resultado

    while True:
        try:
            x = fila.pop(0)
            print('\nCONSUMIDOR: processando tarefa',x)
            time.sleep(2)
            resultado.append(x)
        except:
            time.sleep(2)
            if len(fila) == 0:
                break
  
def Produtor():
    global fila, resultado
       
    for i in range(10):
        fila.append(i)
        tempo=random.random()
        time.sleep(tempo)
        print("PRODUTOR:",tempo)
        print('PRODUTOR: tarefas pendentes:',len(fila),fila)

    while True:
        print('PRODUTOR: tarefas terminadas:',len(resultado),resultado)
        if len(fila) == 0:
           break
        time.sleep(1)
   
if __name__=="__main__": 
    start = time.time() 
       
    t1 = threading.Thread(target=Consumidor)
    t2 = threading.Thread(target=Produtor)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time() 
    print('Time taken in seconds -', end - start)    
