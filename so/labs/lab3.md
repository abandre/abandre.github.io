---
layout: page
title: Atividade Prática 02 - Sistemas Operacionais
---

## Multiprocessing vs Multithreading

Nessa atividade iremos exercitar os conceitos vistos até então nas aulas anteriores. A seguir, um breve resumo:

- Um **programa** é um arquivo executável que consiste em um conjunto de instruções para realizar alguma tarefa e geralmente fica armazenado no disco do seu computador.

- Um **processo** é o que chamamos de programa que foi carregado na memória com todos os recursos de que precisa para operar. Ele tem seu próprio espaço de memória.

- Uma **thread** é a unidade de execução dentro de um processo. Um processo pode ter várias threads em execução como parte dele, onde cada thread usa o espaço de memória do processo e o compartilha com outras threads.

- **Multithreading** é uma técnica em que várias threads são gerados por um processo para fazer diferentes tarefas, quase ao mesmo tempo, apenas uma após a outra. Isso dá a ilusão de que os threads estão sendo executados em paralelo, mas na verdade são executados de maneira simultânea.

- **Multiprocessamento** é uma técnica em que o paralelismo em sua forma mais verdadeira é alcançado. Vários processos são executados em vários núcleos de CPU, que não compartilham os recursos entre eles. Cada processo pode ter muitas threads em execução em seu próprio espaço de memória.

Em Python, vimos implementações de multiprogramação envolvendo tanto multiprocessamento quanto multithreading. Enquanto em python cada processo tem sua própria instância de interpretador Python fazendo o trabalho de execução das instruções, em multithreading, o Global Interpreter Lock (GIL) impede que as threads sejam executados verdadeiramente de forma simultânea.

Para os exercícios a seguir, usaremos duas funções:
1. Função **IO-Bound** - dentro da função IO-bound, pedimos à CPU para ficar ociosa e esperar passar o tempo;
2. Função **CPU-Bound** - dentro da função CPU-bound, a CPU estará ocupada produzindo alguns números.

A seguir está o trecho de código que usaremos nos exercícios:


```python
import time, os 
from threading import Thread, current_thread 
from multiprocessing import Process, current_process 

COUNT = 200000000
SLEEP = 10

def io_bound(sec): 
    pid = os.getpid() 
    threadName = current_thread().name 
    processName = current_process().name 

    print(f"{pid} * {processName} * {threadName} ---> Start sleeping...") 
    time.sleep(sec) 
    print(f"{pid} * {processName} * {threadName} ---> Finished sleeping...") 
  
def cpu_bound(n): 
    pid = os.getpid() 
    threadName = current_thread().name 
    processName = current_process().name 
  
    print(f"{pid} * {processName} * {threadName} ---> Start counting...") 
    while n>0: 
        n -= 1
    print(f"{pid} * {processName} * {threadName} ---> Finished counting...") 
  
if __name__=="__main__": 
    start = time.time() 
  
    # SEU CODIGO VAI AQUI 
  
    end = time.time() 
    print('Time taken in seconds -', end - start) 

```

Note no código anterior, algumas funções bastante úteis em multiprogramação em python, como `os.getpid()` que retorna qual o id do processo em que o trecho de código está sendo executado. Além das funções `current_thread().name` e `current_process().name` que imprimem o nome da thread e do processo correntes.

### Exercício:

Acesse o seguinte <a href="https://forms.office.com/r/1TnSZihJRu" target="_blank">link</a>, siga as instruções e responda às perguntas lá. 

### Leitura complementar

Para quem se interessar, leia esse <a href="https://lih-verma.medium.com/multi-processing-in-python-process-vs-pool-5caf0f67eb2b" target="_blank">artigo</a>. Nele é explicada a adiferença entre **Processos** e **Pool de Processos** em Python. O artigo também explica um pouco sobri o GIL (Global Interpreter Lock) do Python.


<!-- https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/?ref=rp -->
