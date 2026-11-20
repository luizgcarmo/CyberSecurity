import subprocess

# Nome do arquivo de dicionário
DICTIONARY_FILE = "dictionary.txt"

def testar_dicionario():
    # Abrimos o arquivo de dicionário em modo de leitura ('r')
    try:
        with open(DICTIONARY_FILE, 'r') as file:
            # Iteramos linha por linha
            for linha in file:
                # O .strip() remove espaços ou quebras de linha extras ao redor da senha
                senha = linha.strip()
                
                if not senha: # Pula linhas vazias, se houver
                    continue
                
                print(f"Testando a senha: {senha}")
                
                # Executa o nível 5 com a senha do dicionário
                processo = subprocess.run(
                    ["python3", "level5.py"],
                    input=f"{senha}\n",
                    capture_output=True,
                    text=True
                )
                
                # Verifica se a flag apareceu na saída
                if "Welcome back" in processo.stdout.lower() or "user" in processo.stdout.lower():
                    print(f"\n[!!!] SENHA CORRETA ENCONTRADA: {senha}")
                    print(f"[+] Saída: {processo.stdout}")
                    return # Encerra o script ao achar a flag
                    
    except FileNotFoundError:
        print(f"Erro: O arquivo {DICTIONARY_FILE} não foi encontrado.")

if __name__ == "__main__":
    testar_dicionario()