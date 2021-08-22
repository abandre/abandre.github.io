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

def deallocate_mem(pid,memoria):
	for node in memoria:
		if node['pid']==pid:
			index=memoria.index(node)
			print("node anterior:",memoria[index-1])
			print("node atual:",memoria[index])
			print("node posterior:",memoria[index+1])

			if memoria[index-1]['tipo']=='P' and memoria[index-1]['tipo']=='P':
				print("P-P-P")
				memoria[index]['tipo']='H'
				memoria[index]['pid']=-1
			elif memoria[index-1]['tipo']=='H' and memoria[index-1]['tipo']=='P':
				print("H-P-P")
			elif memoria[index-1]['tipo']=='P' and memoria[index-1]['tipo']=='H':
				print("P-P-H")
			else:
				print("H-P-H")
				memoria[index-1]['tamanho']=memoria[index-1]['tamanho']+memoria[index]['tamanho']+memoria[index+1]['tamanho']
				memoria.pop(index+1)
				memoria.pop(index)

#first fit
def allocate_mem(pid,tam,memoria):
	for node in memoria:
		if node['tipo']=='H' and node['tamanho']>=tam:
			index=memoria.index(node)
			if node['tamanho']==tam:
				memoria[index]['tipo']='P'
				memoria[index]['pid']=pid
			else:
				node = {'tipo':'P','inicio':node['inicio'],'tamanho':tam,'pid':pid}
				memoria.insert(index,node)
				memoria[index+1]['inicio']+=tam
				memoria[index+1]['tamanho']-=tam
			return True
	return False

def fragment_count(memoria):
	qtd=0
	for node in memoria:
		if node['tipo']=='H':
			qtd+=1
	return qtd

#memoria = inicializaAleatorio(128)
#print(memoria)
#print("")
#deallocate_mem(5,memoria)
#print("")
#print(memoria)
#allocate_mem(33,5,memoria)
#print("")
#print(memoria)
#print(fragment_count(memoria))

pid=1
falhas=0
memoria = inicializaAleatorio(128)
for i in range(10):
	aleatorio=rnd.randint(0,10)
	if aleatorio > 5:
		tam=rnd.randint(3,10)
		ret = allocate_mem(pid,tam,memoria)
		pid+=1
		if ret==False:
			falhas+=1
	else:
		#TODO desalocar um processo alocado
		deallocate_mem(rnd.randint(1,pid),memoria)

print("fragmentos =",fragment_count(memoria))
print("falhas =",falhas)