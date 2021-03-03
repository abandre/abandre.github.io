---
layout: page
title: Laboratório 01 - Sistemas Operacionais
---

## Processos

O pacote `multiprocessing` suporta processos de spawning, oferecendo simultaneidade local e remota, evitando efetivamente o *Global Interpreter Lock* usando subprocessos em vez de threads. Devido a isso, o módulo de multiprocessamento permite que o programador aproveite totalmente vários processadores em uma determinada máquina. Ele roda em Unix e Windows.

Exemplo de aplicação:

```python
from multiprocessing import Pool
import time

def ola(n):
    time.sleep(10)
    print("ola "+str(n))

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(ola, [1])
    r2 = pool.apply_async(ola, [2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
```

Exercício:

Calcular uma aproximação do valor de 𝜋 a partir da seguinte série:

<img src="formula.png">

De acordo com a série anterior, a precisão do valor de 𝜋 aumenta quanto maior for o parâmetro `N` utilizado.

Como referência, podesmos assumir o valor exato de 𝜋 como sendo o fornecido pela biblioteca `numpy`:

```python
import numpy as np
print(np.pi)
```
O objetivo de exercício é computar uma aprocimação de 𝜋 usando a fórmula anterior para diferentes valores de `N`.

Usando a biblioteca `multiprocessing`, escreva um programa em python que:

- Cria um pool de processos para rodar tarefas em paralelo

- O tamanho do pool deve ser o número de cores da sua CPU menos 1 (8 cores -> pool de 7 processos)

- Escreva uma função que rode em paralelo, chamada py_pi. A função deve receber como parâmetro o valor `N` que especifica o número de termos paa calcular a aproximação de 𝜋.

- A função deve imprimir o valor calculado, o valor real e a diferença do caluclado para o real.

- Rode as tarefas em paralelo, começando com N=10 aumentando 5 vezes para cada processo subsequente (por exemplo: 10, 50, 250, 1250...)


Por fim, espere todos os processos terminarem e imprima o tempo total decorrido.

Para entregar, façam um relatório descrevendo:

- A configuração da sua máquina (principalmente o número de núcleos)
- O tempo total de execução
- Um print do gerenciador de tarefas ou da saída do comando `top` no linux


<!-- https://events.prace-ri.eu/event/549/sessions/1685/attachments/462/667/Exercise_1_-_multiprocessing.pdf -->
