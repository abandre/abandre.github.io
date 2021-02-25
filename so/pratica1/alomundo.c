#include <linux/module.h> 

MODULE_LICENSE("Dual BSD/GPL"); 
MODULE_AUTHOR("Amaury André"); 
MODULE_DESCRIPTION("Um modulo simples!"); 
MODULE_VERSION("0.1"); 

static int alo_inicio(void) {
    printk("Alo, como vai?\n"); 
    return 0; 
} 

static void alo_fim(void) { 
    printk("Adeus, fui!\n"); 
} 

module_init(alo_inicio); 
module_exit(alo_fim);