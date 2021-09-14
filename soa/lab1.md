---
layout: page
title: Laboratório 01
---

##  Alocação de memória principal


**Objetivo:** Simular e avaliar diferentes técnicas de alocação/liberação de memória: first fit, best fit, worst fit.  Usando lista encadeada para gerenciamento de memória.

Suponha que a memória seja de 256 KB e esteja dividida em unidades de 2 KB cada. Um processo pode solicitar entre 3 e 10 unidades de memória. Sua simulação consiste em três componentes: **componente de memória** que implementa uma alocação/liberação específica por técnica; **componente de geração de solicitação** que gera solicitações de alocação/liberação; e **componente de relatório** de estatísticas que imprime as estatísticas relevantes. 

A **componente de memória** exporta as seguintes funções:
- `alocate_mem(process_id, num_units)`: aloca *num_units* unidades de memória para um processo cujo id é *process_id*. Se for bem sucedido, retorna 1. Caso contrário, retorna -1.

- `deallocate_mem(process_id)`: desaloca a memória alocada para o processo cujo id é *process_id*. Ele retorna 1, se for bem-sucedido, caso contrário, -1.

- `fragment_count()`: retorna o número de buracos (fragmentos de tamanhos 1 ou 2 unidades).

Você implementará um componente de memória separado para cada técnica de alocação/liberação. Para solicitações de alocação, o componente especifica o id do processo do processo para o qual a memória é solicitada, bem como o número de unidades de memória sendo solicitada. Para esta simulação, suponha que a memória seja solicitada para cada processo apenas uma vez. Para solicitações de desalocação, o componente especifica o id do processo do processo cuja memória deve ser desalocada. Para esta simulação, suponha que toda a memória alocada para um processo é desalocada em um request de desalocação. Você pode gerar essas solicitações aleatoriamente.

Existem três parâmetros de desempenho que sua simulação deve calcular para cada
técnica: número médio de fragmentos externos, tempo médio de alocação em termos de número médio de nós percorridos na alocação, e a porcentagem de vezes que um pedido de alocação negado.

Gere 10.000 solicitações usando o **componente de geração de solicitação** e, para cada solicitação, invocar a função apropriada do componente de memória para cada uma das técnica de alocação/liberação. Após cada solicitação, atualize as três performances parâmetros para cada uma das técnicas.

O **componente de relatório de estatísticas** imprime o valor dos três parâmetros para todos os quatro técnicas no final.

Entregar o relatório final de comparação entre as técnicas utilizadas, juntamente com uma avaliação crítica desse resultado.

A seguir, uma estrutura básica de sugestão para a representação da memória, de inicialização aleatória, para percorrer a lista e encontrar um processo (seu antecessor e sucessor).

```python
import random as rnd

def inicializa(tamanho):
	memoria=[]
	node = {'tipo':'H','inicio':0,'tamanho':tamanho,'pid':-1}
	memoria.append(node)

	return memoria

def inicializaAleatorio(tamanho):
	posicao=0
	memoria=[]
	i=0
	p=1
	while posicao<tamanho:
		tam=rnd.randint(3,10)
		if posicao+tam>tamanho:
			tam=tamanho-posicao

		if i%2==0:
			tipo='P'
			pid=p
			p+=1
		else:
			tipo='H'
			pid=-1

		node = {'tipo':tipo,'inicio':posicao,'tamanho':tam,'pid':pid}
		memoria.append(node)
		posicao+=tam
		i+=1

	return memoria

def deallocate_mem(pid): # TODO
	global memoria

	for node in memoria:
		if node['pid']==pid:
			index=memoria.index(node)

			# verificacao de limite inferior da memoria
			if index>0:
				anterior = memoria[index-1]
			else:
				anterior = memoria[0]

			# verificacao de limite superior da memoria
			if index<len(memoria)-1:
				posterior = memoria[index+1]
			else:
				posterior = memoria[len(memoria)-1]

			print("node anterior:",anterior)
			print("node atual:",node)
			print("node posterior:",posterior)
		
			if anterior['tipo']=='P' and posterior['tipo']=='P':
				# troco P p/ H e atualizo o pid
				pass
			elif anterior['tipo']=='P' and posterior['tipo']=='H':
				# emendo com o buraco posterior
				pass
			elif anterior['tipo']=='H' and posterior['tipo']=='P':
				# emendo com o buraco anterior
				pass
			elif anterior['tipo']=='H' and posterior['tipo']=='H':
				# emendo com os buracos anterior e posterior
				pass




def allocate_mem_first_fit(pid,tamanho):
	global memoria

	for node in memoria:
		if node['tipo']=='H':
			if node['tamanho']==tamanho:
				# trocar P por H
				# atualizar pid
				break
			elif node['tamanho']>tamanho:
				# # criar um no p/ o processo: 
				# index=memoria.index(node)
				# novo = {'tipo':'P','inicio':???,'tamanho':???,'pid':???}
				# memoria.insert(index,novo)

				# # atualizar o inicio e o tamanho do buraco
				# node['inicio']=???
				# node['tamanho']=???
				break			


def allocate_mem_best_fit(pid,tamanho):
	pass

def allocate_mem_worst_fit(pid,tamanho):
	pass
	

memoria = inicializa(128)
print(memoria)
print()

allocate_mem_firstfit(1,5)
print(memoria)
print()

deallocate_mem(1)
print(memoria)
print()

# exemplo para gerar aleatoriamente uma sequencia
# pid=1
# processos_alocados=[]
# for i in range(10):
# 	moeda = rnd.randint(0,1)
# 	print(moeda)	

# 	if moeda==1:
# 		tam=rnd.randint(3,10)
# 		print("alocar processo",pid,"com tamanho",tam)
# 		#allocate_mem_first_fit(pid,tam)		
# 		processos_alocados.append(pid)
# 		pid+=1
# 	else:
# 		if len(processos_alocados)>0:
# 			idx=rnd.randint(0,len(processos_alocados)-1)
# 			#deallocate_mem(processos_alocados[idx])
# 			print("desalocar processo",processos_alocados[idx])
# 			processos_alocados.pop(idx)		

```