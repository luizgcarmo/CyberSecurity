import sys
import multiprocessing as mp
from passlib.hash import sha512_crypt

# Configurações do Desafio
TARGET_HASH = "$6$gGponKq7GDAyn1B5$NEmyZgWd3sBOxiJZ0KHKibt9PBZFKOP3/THbdSer4lmvNfFmBhuW/QaWrIsAXZGD511yxj0BVRbJFygDesPQj1"
WORDLIST_PATH = "/usr/share/wordlists/rockyou.txt"
CHUNK_SIZE = 10000  # Tamanho do lote de palavras enviado a cada núcleo

def check_word(word):
    """Função executada em paralelo para validar uma senha"""
    word = word.strip()
    if not word:
        return None
    try:
        if sha512_crypt.verify(word, TARGET_HASH):
            return word
    except Exception:
        pass
    return None

def main():
    # Detecta quantos núcleos de CPU estão disponíveis na máquina
    num_workers = mp.cpu_count()
    print(f"[*] Utilizando {num_workers} núcleos de CPU para busca paralela...")
    print(f"[*] Analisando {WORDLIST_PATH}...")

    with open(WORDLIST_PATH, "r", encoding="latin-1") as f:
        # Cria um pool de processos de acordo com os núcleos da CPU
        with mp.Pool(processes=num_workers) as pool:
            # imap_unordered distribui o arquivo em blocos na memória sem criar arquivos temporários
            for result in pool.imap_unordered(check_word, f, chunksize=CHUNK_SIZE):
                if result:
                    print(f"\n[+] SENHA ENCONTRADA: {result}")
                    pool.terminate()  # Encerra os outros processos imediatamente
                    sys.exit(0)

    print("\n[-] Senha não encontrada na wordlist.")

if __name__ == "__main__":
    main()