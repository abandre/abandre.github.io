#include <linux/module.h> 

MODULE_LICENSE("Dual BSD/GPL"); 

static int numero;
module_param(numero, int, 0);

static char *texto = "Ola!";
module_param(texto, charp, 0);

static int alo_inicio(void) {
	int i;
	for (i=0;i<numero+1;i++) {
		printk(texto);
	}  
    return 0; 
} 

static void alo_fim(void) { 
    printk("Adeus, Mundo Cruel!\n"); 
} 


module_init(alo_inicio); 
module_exit(alo_fim);