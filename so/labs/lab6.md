---
layout: page
title: Laboratório 06 - Sistemas Operacionais
---

## Sincronização - Eventos e Condições

Neste laboratório vamos explorar o problema de Produtor vs Consumidor visto em aula. Para tanto, utilizaremos como base o seguinte trecho de código python.


```python
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
```

Note no código acima, que o produtor insere elementos na fila, enquanto o consumidor retira os elementos da fila e os insere em resultado. Note que, devido as velocidades diferentes entre a produção e o consumo, o produtor acaba sobrecarregando o consumidor, fazendo com que os itens vão se acumulando na fila.

## Exercício 1

Utilizado a sincronização por evento, faça com que o Produtor não sobrecarregue o Consumidor com mais de **duas** tarefas pendentes.

Lembrando que, a primitiva de sincronização de eventos atua como um comunicador simples entre as threads. Eles são baseados em um sinalizador interno que as threads podem definir `set()` ou limpar `clear()`. Outras threads podem esperar `wait()` para que o sinalizador interno seja definido. O método `wait()` bloqueia até que o sinalizador se torne verdadeiro. 

Python implementa eventos usando `threading.Event()`

threading.Event() opera da seguinte forma:

- no programa principal, antes da chamada das threads: `evento = threading.Event()`
- uma thread pode dormir até que um evento aconteça: `evento.wait()`
- uma thread pode acordar a thread que estava dormindo gerando um evento: `evento.set()`
- após gerar o evento, ele pode ser removido para travar a thread caso ela chame wait novamente: `evento.clear()`

## Exercício 2

Crie um segundo produtor na solução gerada para o exercício 3. Faça com que o segundo produtor crie tarefas com os números 11 até 20, como a seguir.

```python
def Produtor2():
    global fila, resultado
       
    for i in range(11,20):
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
```

### a) Utilizado a sincronização por evento, faça com que os produtores não sobrecarregue o consumidor com mais de duas tarefas pendentes.

### b) Responda a pergunta: o evento acorda um ou os dois produtores simultaneamente?

### c) Substitua o mecanismo de Evento por Condição e verifique novamente se os dois produtores são acordados simultaneamente (através do método `notify`).

Lembrando que um objeto `Condition` é simplesmente uma versão mais avançada do objeto `Event`. Ele também atua como um comunicador entre threads e pode ser usado para notificar `notify()` outras threads sobre uma mudança no estado do programa. Por exemplo, pode ser usado para sinalizar a disponibilidade de um recurso para consumo. Outras threads também devem adquirir `acquire()` a condição (e, portanto, seu bloqueio relacionado) antes de esperar `wait()` que a condição seja satisfeita. Além disso, um encadeamento deve liberar `release()` uma condição depois de concluir as ações relacionadas, para que outras threads possam adquirir a condição para seus propósitos.

Python implementa condições usando `threading.Condition()`.

- no programa principal, antes da chamada das threads: `condition = threading.Condition()`
- uma ou mais threads entram em estado de espera:

```python
condition.acquire()
condition.wait()
condition.release()
```

- o programa principal ou outra thread pode acordar todas as threads simultaneamente:

```python
condition.acquire()
condition.notify() ou condition.notifyAll()
condition.release()
```

- `notify` acorda uma única thread e `notifyAll` todas as threads simultaneamente.


<!-- https://www.ppgia.pucpr.br/~jamhour/Pessoal/Graduacao/Ciencia/Python/SincProcessos.html -->
