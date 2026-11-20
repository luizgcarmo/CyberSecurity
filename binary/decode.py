if __name__ == "__main__":

	# Salve o hexdump que você tem em um arquivo chamado 'data.bin'
	with open('data.bin', 'rb') as f:
    		data = f.read()

	# Tenta todas as chaves de 0 a 255
	for key in range(256):
		decoded = bytes([b ^ key for b in data])
		if b'picoCTF' in decoded:
        		print(f"Chave encontrada: {key}")
        		print(f"Flag: {decoded.decode(errors='ignore')}")
        		break
        
        