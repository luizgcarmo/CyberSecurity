# 🛡️ Portfólio de Estudos e Práticas em Cibersegurança

Este repositório documenta minha evolução técnica, laboratórios práticos e resoluções de desafios de **Capture The Flag (CTF)**, com foco em fundamentos de análise de segurança, investigação forense, engenharia reversa e exploração de vulnerabilidades.

---

## 🎯 Objetivo Profissional
Consolidar habilidades técnicas práticas para atuação como **Analista de Segurança da Informação Júnior**, aplicando metodologias de análise de artefatos, triagem de incidentes, perícia digital e compreensão de vetores de ataque.

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
# 🐧 Administração, Troubleshooting e Uso Avançado de Linux

Este documento reúne os conhecimentos práticos adquiridos no uso diário e na administração do ambiente **BlackArch / Arch Linux**, com foco em linha de comando (CLI), automação via Bash, gerenciamento de pacotes e manipulação de sistemas de arquivos.

---

## 💻 Ambiente Principal
* **Distribuição:** BlackArch Linux (baseado em Arch Linux)
* **Shell:** Bash (GNU Bourne-Again SHell)
* **Foco:** Segurança Ofensiva/Defensiva, Forense Digital e Automação de Terminal

---

## ⚙️ Competências Técnicas em Linux

### 1. Manipulação Avançada de Arquivos e Busca (CLI)
Domínio de utilitários nativos do Linux para triagem rápida de grandes volumes de arquivos e logs:
* **Busca Recursiva e Filtragem:** Uso combinado de `find`, `grep` (flags `-r`, `-n`, `-i`, `-C`, `-E`) para localizar padrões específicos em diretórios complexos e arquivos compactados (`unzip -l`).
* **Inspeção de Arquivos e Binários:** Identificação de tipos de arquivo independentemente da extensão (`file`), leitura paginada (`less`), visualização de conteúdo (`cat`), comparação byte a byte (`cmp -l`) e manipulação de blocos (`dd`).
* **Codificação via Terminal:** Conversão e decodificação rápida de fluxos de dados utilizando `base64 -d`, `xxd` e `hexdump -C`.

### 2. Gerenciamento de Sistemas de Arquivos e Dispositivos
* **Montagem e Dispositivos de Loop:** Criação manual e montagem de imagens de disco em modo somente leitura (`mount -o loop,ro,offset=...`, `losetup`) para análise segura sem alteração de integridade.
* **Diagnóstico de Partições:** Cálculo de *offsets* de setores e identificação de estruturas de sistemas de arquivos (`ext2/3/4`, `FAT`, `NTFS`).

### 3. Shell Scripting e Automação no `.bashrc`
Desenvolvimento de rotinas personalizadas para aumento de produtividade e monitoramento de tarefas no terminal:
* **Automação de Notificações:** Criação de funções e *aliases* personalizados no `~/.bashrc` integrando notificações visuais (`notify-send`) e alertas sonoros (`paplay` / `ffmpeg`) para conclusão de comandos de longa duração.
* **Gerenciamento de Processos e Subshells:** Execução de tarefas em segundo plano (`&`), controle de jobs e supressão de ruídos de saída de subshells.
* **Autostart de Ambiente Gráfico:** Configuração de arquivos `.desktop` em `~/.config/autostart/` para inicialização automática de serviços e scripts de sessão no XFCE.

### 4. Administração de Pacotes e Resolução de Conflitos (Arch/BlackArch)
* **Gerenciamento com `pacman` e AUR (`yay`):** Instalação, atualização de sistema (`pacman -Syu`) e compilação de pacotes comunitários.
* **Troubleshooting de Dependências:** Diagnóstico e resolução de conflitos de bibliotecas compartilhadas (ex: conflitos entre `libjpeg` e `libjpeg-turbo` em ferramentas como `steghide`).
* **Gestão de Ambientes Java (JVM):** Configuração de múltiplas versões do OpenJDK (`/usr/lib/jvm/`) e resolução de incompatibilidades de módulos (como `JavaFX` e *Security Manager*) para execução de ferramentas forenses legadas como o Autopsy.

### 5. Diagnóstico de Hardware e Sistema
* **Inventário e Monitoramento:** Verificação de arquitetura e especificações de processador (`lscpu`, `/proc/cpuinfo`, `inxi -C`, `lshw`) e acompanhamento de recursos e processos em tempo real (`htop`, `watch`).
* **Servidor de Áudio e GUI:** Diagnóstico de subsistemas de áudio (ALSA vs. PipeWire/PulseAudio) e gerenciamento/redefinição de ambientes gráficos (XFCE, GNOME, KDE).

## 🛠️ Ferramentas Utilizadas nos Laboratórios
* **Forense & Carving:** Autopsy, The Sleuth Kit (TSK), ExifTool, Binwalk, Steghide, Stegsolve, Zsteg.
* **Debugging & Disassembly:** GDB, Objdump, xxd, Hexdump, Strings.
* **Desenvolvimento & Automação:** Python 3, Pwntools, Regex/Grep.
* **Plataformas de Treinamento:** picoCTF, CyLab Academy, ambientes CTF locais.
