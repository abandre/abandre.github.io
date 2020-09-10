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

memoria = inicializaAleatorio(128)
print(memoria)
print("")
deallocate_mem(5,memoria)
#allocate_mem(33,5,memoria)
#print(memoria)

