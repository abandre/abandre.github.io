---
layout: page
title: Aula Prática 01 - Sistemas Operacionais Abertos
---

## Informações do Sistema em Linux

### Nome do sistema

- `hostname`

### Número de série, fabricante e modelo

- `sudo dmidecode -s system-serial-number`

- `sudo dmidecode -s system-manufacturer`

- `sudo dmidecode -s system-product-name`

### Mais informações de hardware

- `sudo dmidecode | more`

- `lshw | more`

### Informações específicas sobre a CPU

- `cat /proc/cpuinfo`

- `lscpu`

### Informações sobre memória

- `free -h`

- `swapon -s`

- `vmstat`

### Versão do Sistema Operacional

- `lsb_release -a`

- `uname -a`

### Informações sobre o Discos

- `sudo fdisk -l`

- `lsblk`

- `df -h`

- `du -h`

### Informações sobre outros dispositivos

- `lspci`

- `lsusb`

- `iwconfig`

- `lspci | grep -i vga`

- `lspci | grep -i audio`

- `nvidia-smi`

### Resumo

- `sudo apt-get install inxi`

- `inxi -F`


