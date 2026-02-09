import threading 
import numpy as np

def py_exp(y,N): 
    aproximacao_exp=0
    for i in range(N):
        den=1
        for j in range(1,i+1):
            den*=j
       # print(i,den)
        aproximacao_exp+=pow(y,i)/den
  
    print(aproximacao_exp,np.exp(y),np.exp(y)-aproximacao_exp)

if __name__ == "__main__": 
    num_threads = 7

    threads = []
    valores_N = []
    N=10000
    y=10
    for i in range(num_threads):
        t = threading.Thread(target=py_exp, args=(y,N,))
        t.start() 
        threads.append(t)
        valores_N.append(N)
        y+=2
     
    for i in range(num_threads):
        threads[i].join()   
    
    print("Done!") 