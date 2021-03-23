---
layout: page
title: Laboratório 05 - Sistemas Operacionais
---

## Sincronização - Semáforos

Os semáforos são como contadores avançados. Uma chamada `acquire()` a um semáforo irá bloquear somente depois que um número máximo de threads já tiver chamado `acquire()`. 

Um contador associado diminui por cada chamada de `acquire()` feita e aumenta por cada chamada de `release()`. Um `ValueError` ocorrerá se as chamadas de `release()` tentarem incrementar o contador além de seu valor máximo atribuído (que é o número de threads que podem fazer o `acquire()` do semáforo antes de ocorrer o bloqueio). 

Os semáforos são normalmente usados ​​para limitar um recurso, como limitar um servidor para lidar com apenas 10 clientes por vez. Nesse caso, várias conexões de thread competem por um recurso limitado (em nosso exemplo, é o servidor).

O código a seguir demonstra o problema de produtor-consumidor:

```python
from threading import Thread
import time
import random

g = 0

def incrementa():
    global g

    tmp = g     # le valor
    tmp += 1    # incrementa
    g = tmp     # escreve

if __name__=="__main__": 
    thread1 = Thread(target=incrementa)
    thread1.start()

    thread2 = Thread(target=incrementa)
    thread2.start()

    thread1.join()
    thread2.join()

    print(g)
```

Para resolver o problema de *Heisenbug* visto, uma forma seria a de transformar a função de incrementar em uma região crítica. Para isso, podemos usar Locks. Para isso precisamos importar a biblioteca, e declarar uma variável de trava, juntamente com a variável global compartilhada:

```python
from threading import Lock

g=0
lock = Lock()
```

Com isso, protegemos uma região crítica pegando a trava antes de iniciar e liberando a trava após terminar, através dos seguintes comandos:

```python
lock.acquire()
# codigo da regiao critica
lock.release()
```

### Exercício:

Acesse o seguinte <a href="https://forms.office.com/r/Pr09s3zJdh" target="_blank">link</a>, siga as instruções e responda às perguntas lá. O formulário estará disponível durante o horário de aula somente.




<!-- https://betterprogramming.pub/synchronization-primitives-in-python-564f89fee732 -->
