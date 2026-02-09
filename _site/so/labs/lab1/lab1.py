from multiprocessing import Pool
import time
import numpy as np

def py_pi(N):
    aproximacao_pi=0
    for i in range(1,N):
        aproximacao_pi+= 1 / (1+ pow((i-0.5)/N,2) )
    aproximacao_pi*=(4/N)

    print(N,aproximacao_pi,np.pi,np.pi-aproximacao_pi)

    return aproximacao_pi

if __name__ == '__main__':
    numero_processos=7
    pool = Pool(processes=numero_processos)
    start = time.time()

    processos = []
    valores_N = []

    N=10000
    for i in range(numero_processos):
        processos.append(pool.apply_async(py_pi, [N]))
        valores_N.append(N)
        N*=5
        N=int(N)
    
    pool.close()
    pool.join()

    print(50*"-")

    for i in range(numero_processos):
        resultado = processos[i].get()
        valor_N = valores_N[i]
        print(valor_N,resultado,np.pi,np.pi-resultado)


    end = time.time()
    print('Time taken in seconds -', end - start)
