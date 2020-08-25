#include <linux/module.h> 

MODULE_LICENSE("Dual BSD/GPL"); 

static int alo_inicio(void) { 
    printk("Alo, Mundo!\n"); 
    return 0; 
} 

static void alo_fim(void) { 
    printk("Adeus, Mundo Cruel!\n"); 
} 

module_init(alo_inicio); 
module_exit(alo_fim);