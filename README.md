# 🛡️ Portfólio de Estudos e Práticas em Cibersegurança

Este repositório documenta minha evolução técnica, laboratórios práticos e resoluções de desafios de **Capture The Flag (CTF)**, com foco em fundamentos de análise de segurança, investigação forense, engenharia reversa e exploração de vulnerabilidades.

---

## 🎯 Objetivo Profissional
Consolidar habilidades técnicas práticas para atuação como **Analista de Segurança da Informação / SOC N1 Júnior**, aplicando metodologias de análise de artefatos, triagem de incidentes, perícia digital e compreensão de vetores de ataque.

---

## 📚 Áreas de Estudo e Habilidades Técnicas

### 1. Forense Digital (DFIR) e Análise de Disco
Investigação de imagens de disco, recuperação de evidências e análise de sistemas de arquivos para reconstrução de eventos.
* **The Sleuth Kit (TSK) & Autopsy:** Análise em nível de volume e sistema de arquivos (`mmls`, `fls`, `icat`, `tsk_recover`, `blkls`, `mactime`) para localização de arquivos ocultos, histórico de comandos (`.bash_history`) e recuperação de arquivos deletados em imagens `.img`.
* **Aquisição e Carving:** Conceitos de preservação de evidências, análise de espaço não alocado (*unallocated space*) e recuperação por assinatura de cabeçalho com `binwalk` e `dd`.
* **Análise de Estruturas de Boot:** Inspeção de sistemas embarcados/mínimos (*initramfs* e Alpine Linux).

### 2. Forense de Imagens e Esteganografia
Inspeção de arquivos multimídia para detecção de adulterações e extração de dados ocultos.
* **Análise de Metadados:** Extração e leitura de tags EXIF e campos personalizados com `exiftool`.
* **Análise Binária e Hexadecimal:** Inspeção de *magic bytes*, cabeçalhos de arquivos (ex: assinaturas `MZ` e `PE`), extração de strings legíveis (`strings`) e leitura de dumps hexadecimais (`xxd`, `hexdump`).
* **Esteganografia:** Detecção de dados embutidos e análise de planos de bits/cores utilizando `binwalk`, `steghide`, `stegsolve` e `zsteg`.

### 3. Segurança Web e Inspeção de Protocolos
* **Análise de Sessão e Armazenamento:** Inspeção e manipulação de *Cookies* e armazenamento local via ferramentas de desenvolvedor (DevTools) para identificação de tokens e dados sensíveis expostos.
* **Codificação e Criptografia Básica:** Identificação e decodificação de strings em Base64, conversão Hexadecimal/Decimal e compreensão de criptografia simétrica com tokens **Fernet** (chaves de 32 bytes em Base64).

### 4. Análise de Binários, Engenharia Reversa e Exploração (Pwn)
Compreensão de baixo nível sobre como falhas de memória ocorrem (essencial para entender regras de detecção e assinaturas de exploits).
* **Análise Estática e Dinâmica:** Desmontagem de binários x86-64 com `objdump` (análise de instruções assembly como `xor`, `cmp`, `je`/`jne`) e depuração em tempo real com **GDB** (mapeamento de memória com `info proc map`, inspeção de registradores e funções).
* **Mitigações de Binários:** Identificação de proteções de compilação (ASLR, PIE, Stack Canary, NX, Full RELRO).
* **Exploração de Format String:** Identificação de vazamento de memória da stack (`%p`), cálculo de *offset* dinâmico, bypass de PIE (*Position Independent Executable*) e escrita arbitrária na memória (`%hhn`).
* **Automação com Python (`pwntools`):** Desenvolvimento de scripts para interação com serviços remotos, empacotamento de endereços em 64-bit (`p64`) e automação de payloads.

### 5. Fundamentos de Red Team & Detecção (Blue Team)
* **Arquitetura C2 (Command & Control):** Estudo teórico do funcionamento de frameworks C2 (como *Sliver C2*), comunicação cliente-servidor (*listeners* HTTP/HTTPS/mTLS, *beacons* e *sessions*) e indicadores de comprometimento (IoCs) gerados no tráfego de rede e processos.

---

## 🛠️ Ferramentas Utilizadas nos Laboratórios
* **Forense & Carving:** Autopsy, The Sleuth Kit (TSK), ExifTool, Binwalk, Steghide, Stegsolve, Zsteg.
* **Debugging & Disassembly:** GDB, Objdump, xxd, Hexdump, Strings.
* **Desenvolvimento & Automação:** Python 3, Pwntools, Regex/Grep.
* **Plataformas de Treinamento:** picoCTF, CyLab Academy, ambientes CTF locais.
