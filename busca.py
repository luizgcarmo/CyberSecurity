import os
import re

# Padrões comuns que atacantes buscam em servidores comprometidos
PADROES = {
    "SSH Private Key": r"-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic Password String": r"(?i)(password|senha|secret_key)\s*=\s*['\"][^'\"]+['\"]",
}

diretorio_alvo = "/home"

for root, dirs, files in os.walk(diretorio_alvo):
    for file in files:
        caminho = os.path.join(root, file)

        # Ignorar arquivos muito grandes para manter o script rápido e discreto
        try:
            if os.path.getsize(caminho) > 5 * 1024 * 1024:  # > 5MB
                continue

            with open(caminho, "r", errors="ignore") as f:
                conteudo = f.read()
                for nome_padrao, regex in PADROES.items():
                    if re.search(regex, conteudo):
                        print(
                            f"[!] [ALVO ENCONTRADO] Tipo: {nome_padrao} | Arquivo: {caminho}"
                        )

        except Exception:
            continue