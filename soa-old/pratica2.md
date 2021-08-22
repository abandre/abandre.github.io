---
layout: page
title: Aula Prática 02 - Sistemas Operacionais Abertos
---

## Módulos do Kernel no Linux

Vimos em aula que módulos são arquivos-objeto, parte do kernel, que são vinculados a ele em tempo de execução.

Um módulo no linux é um código, geralmente drivers de dispositivos que podem ser carregados e descarregados sem a necessidade de reiniciar o sistema.

Os módulos podem ser inseridos e removidos em um kernel em execução a qualquer tempo, exceto quando em uso.

Os arquivos de drivers geralmente terminam com a extensão .ko (ou .o) e são armazenados em subdiretórios dentro de /lib/modules

### Comandos para Gerenciamento de Módulos

 - `depmod` - Trabalha com dependências dos módulos
 - `insmod` - Carrega módulos em um kernel em execução
 - `lsmod`  - Lista informações sobre módulos carregados
 - `modinfo` - Lista informações sobre um módulo
 - `modprobe` - Carrega, descarrega e gera relatórios em módulos, e trata de suas dependências
 - `rmmod` - Descarrega módulos de um kernel em execução

### Criando um módulo no Linux

 - são executados no espaço do kernel;
 - só podem executar funções definidas pelo kernel;
 - são orientados a eventos (executam uma determinada tarefa apenas quando recebem uma solicitação);
 - possuem uma função de inicialização que o prepara para receber as solicitações;
 - possuem uma função de finalização que libera os recursos alocados antes da desinstalação.

Exemplo, Hello World!

```c
#include <linux/module.h> 

MODULE_LICENSE("Dual BSD/GPL"); 
MODULE_AUTHOR("Amaury André"); 
MODULE_DESCRIPTION("Um modulo simples!"); 
MODULE_VERSION("0.1"); 

static int alo_inicio(void) {
    printk("Alo, Mundo!\n"); 
    return 0; 
} 

static void alo_fim(void) { 
    printk("Adeus, Mundo Cruel!\n"); 
} 

module_init(alo_inicio); 
module_exit(alo_fim);
```

 - `MODULE_LICENSE()` – esta macro informa a licença do módulo (no exemplo, o código é disponibilizado sob as licenças BSD e GPL).
 - `module_init()` – macro que define quais funções são chamadas quando o módulo é carregado. Neste exemplo, apenas a função alo_inicio() é chamada.
 - `module_exit()` – macro que define quais funções são chamadas antes do módulo ser removido. Neste exemplo, apenas a função alo_fim() é chamada.
 - `printk()` – função que escreve mensagens do kernel em /var/log/syslog.

Para compilar e gerar o arquivo .ko do módulo, crie o arquivo Makefile.

```shell
obj-m := alomundo.o 

all: 
       make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules 

clean: 
       make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```
 - obj-m – especifica os arquivos-objeto que serão usados para gerar os módulos carregáveis do kernel. Neste exemplo, será usado o arquivo alomundo.o para gerar o arquivo alomundo.ko.
- -C diretório – esta opção muda para o diretório especificado antes de ler o Makefile (vai usar esse ambiente na geração dos módulos).
- M diretório modules – vai para o diretório especificado antes de gerar os módulos (os arquivos serão armazenados nesse diretório).

### Carregando o módulo

- `sudo insmod alomundo.ko`

### Verificando o módulo

- `lsmod`

- `less /proc/modules`

### Informações do módulo

- `modinfo alomundo.ko`

### Removendo o módulo

- `sudo rmmod alomundo`

### Log do sistema

- `dmesg`


### Parâmetros

Passados em user-space para o insmod/modprobe.

Exemplo:

- `insmod meu_modulo.ko numero=3`

Tipos de dados padrão:

- Byte
- (u)short
- (u)int
- (u)long
- charp
- Bool

Exemplo:

```c
static int numero;
module_param (numero, int, 0);
```

### Exercício Extra:

Criar 1 módulo que recebe um número inteiro e uma string como parâmetro e imprime a string o número desejado de vezes.

### Conclusão

Vimos neste artigo alguns comandos relacionados a módulos do Linux. Este assunto é parte do tópico 101 da certificação Linux LPIC-1.

