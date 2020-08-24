---
layout: page
title: Laboratório 01 - Sistemas Operacionais Abertos
---

## Processos versus Threads

Vimos em aula os conceitos de ULT (Threads de Usuário) e KLT (Threads de núcleo).

<img src="/soa/ultklt.png">

Na linguagem de programação Python, devido a uma característica chamada Python Global Interpreter Lock (GIL), a linguagem oferece o conceito de multithreading somente a nível de usuário. O GIL, em poucas palavras, é um mutex que permite que apenas uma thread mantenha o controle do interpretador Python. Isso significa que apenas uma thread pode estar em um estado de execução a qualquer momento.

Para mostrar isso, observe o seguint trecho de código, que faz uma contagem regressiva:

```python
# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
```

Agora, observe o código a seguir, que divide a contagem entre duas threads:

```python
# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
```
### 1. Qual a configuração da sua máquina? 

### 2. Qual deveria ser a diferença de tempo entre as duas rotinas apresentadas (single e multithreaded)?

### 3. Qual foi a diferença no tempo de execução em sua máquina?

### 4. Qual o tempo de execução para a seguinte rotina?

```python
from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
```

### 5. O que difere da rotina anterior para a rotina multithreaded apresentada, que faz com que essa diferença no tempo de execução aconteça?

