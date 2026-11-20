from pwn import *

print("=== Calculadora de Endereços com PIE ===")

# 1. Entrada interativa para os valores locais (pegos no GDB)
local_win = int(input("Digite o endereço local da função WIN (ex: 0x5555555552aa): "), 16)
local_main = int(input("Digite o endereço local da MAIN (ex: 0x55555555534c): "), 16)

# 2. Entrada interativa para o endereço vazado pelo servidor
servidor_main_str = input("Digite o endereço da MAIN vazado pelo servidor (ex: 0x611fadff334c): ")
servidor_main = int(servidor_main_str, 16)

# 3. Cálculo automático
offset = local_main - local_win
servidor_win = servidor_main - offset

# 4. Resultado
print("\n" + "="*40)
print(f"[*] Offset calculado: {hex(offset)}")
print(f"[+] Endereço real da WIN no servidor: {hex(servidor_win)}")
print("="*40)
