import hashlib

# O nome de usuário que está no código trial
username = b"BENNETT"

# Gerando o hash SHA256 exatamente como o programa faz
h = hashlib.sha256(username).hexdigest()

# A ordem dos índices definida no seu script original
# (Confirmada pelo que você passou anteriormente)
indices = [4, 5, 3, 6, 2, 7, 1, 8]

# Construindo a parte dinâmica
dinamica = "".join([h[i] for i in indices])

# Montando a flag completa
flag = "picoCTF{1n_7h3_kk3y_of_" + dinamica + "}"

print(f"A chave esperada é: {flag}")