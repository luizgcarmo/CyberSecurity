# 🛡️ Cybersecurity Studies & Hands-on Portfolio

This repository documents my technical progression, hands-on labs, and **Capture The Flag (CTF)** challenge write-ups, focusing on security analysis fundamentals, digital forensics, reverse engineering, and vulnerability exploitation.

---

## 🎯 Career Objective
Consolidate practical technical skills to work as a **Junior SOC Analyst / Tier 1 Information Security Analyst**, applying artifact analysis methodologies, incident triage, digital forensics, and a solid understanding of attack vectors.

---

## 📚 Study Areas & Technical Skills

### 1. Digital Forensics (DFIR) & Disk Analysis
Investigation of disk images, evidence recovery, and file system analysis for event reconstruction.
* **The Sleuth Kit (TSK) & Autopsy:** Volume and file system level analysis (`mmls`, `fls`, `icat`, `tsk_recover`, `blkls`, `mactime`) to locate hidden files, command history (`.bash_history`), and recover deleted files from `.img` disk images.
* **Acquisition & Carving:** Evidence preservation concepts, unallocated space analysis, and header signature file carving using `binwalk` and `dd`.
* **Boot Structure Analysis:** Inspection of embedded and minimal Linux file systems (*initramfs* and Alpine Linux).

### 2. Image Forensics & Steganography
Inspection of multimedia files to detect tampering and extract hidden data.
* **Metadata Analysis:** Extraction and reading of EXIF tags and custom fields using `exiftool`.
* **Binary & Hexadecimal Analysis:** Inspection of *magic bytes* and file headers (e.g., `MZ` and `PE` signatures), extraction of readable strings (`strings`), and analysis of hex dumps (`xxd`, `hexdump`).
* **Steganography:** Detection of embedded data and bit/color plane analysis using `binwalk`, `steghide`, `stegsolve`, and `zsteg`.

### 3. Web Security & Protocol Inspection
* **Session & Storage Analysis:** Inspection and manipulation of *Cookies* and browser local storage via Developer Tools (DevTools) to identify exposed tokens and sensitive data.
* **Encoding & Basic Cryptography:** Identification and decoding of Base64 strings, Hexadecimal/Decimal conversions, and understanding symmetric encryption using **Fernet** tokens (32-byte Base64-encoded keys).

### 4. Binary Analysis, Reverse Engineering & Exploitation (Pwn)
Low-level understanding of how memory corruption flaws occur (essential for understanding detection rules and exploit signatures).
* **Static & Dynamic Analysis:** Disassembly of x86-64 binaries using `objdump` (analyzing assembly instructions such as `xor`, `cmp`, `je`/`jne`) and real-time debugging with **GDB** (memory mapping via `info proc map`, inspecting registers and functions).
* **Binary Mitigations:** Identification of compiler protections (ASLR, PIE, Stack Canary, NX, Full RELRO).
* **Format String Exploitation:** Identification of stack memory leaks (`%p`), dynamic *offset* calculation, PIE (*Position Independent Executable*) bypass, and arbitrary memory write (`%hhn`).
* **Automation with Python (`pwntools`):** Scripting interactions with remote services, 64-bit address packing (`p64`), and payload automation.

### 5. Red Team & Detection Fundamentals (Blue Team)
* **C2 (Command & Control) Architecture:** Theoretical study of C2 frameworks (such as *Sliver C2*), client-server communication (HTTP/HTTPS/mTLS *listeners*, *beacons*, and *sessions*), and Indicators of Compromise (IoCs) generated in network traffic and host processes.

---

## 🛠️ Lab Tools & Technologies
* **Forensics & Carving:** Autopsy, The Sleuth Kit (TSK), ExifTool, Binwalk, Steghide, Stegsolve, Zsteg.
* **Debugging & Disassembly:** GDB, Objdump, xxd, Hexdump, Strings.
* **Development & Automation:** Python 3, Pwntools, Regex/Grep.
* **Training Platforms:** picoCTF, CyLab Academy, local CTF environments.

# 🐧 Linux Administration, Troubleshooting & Advanced CLI Usage

This document compiles the practical knowledge acquired through daily usage and administration of a **BlackArch / Arch Linux** environment, focusing on command-line interface (CLI) mastery, Bash automation, package management, and file system manipulation.

## 💻 Primary Environment

* **Distribution:** BlackArch Linux (Arch Linux-based)
* **Shell:** Bash (GNU Bourne-Again SHell)
* **Focus:** Offensive/Defensive Security, Digital Forensics, and Terminal Automation

## ⚙️ Technical Linux Competencies

### 1. Advanced File Manipulation & Search (CLI)
Proficiency in native Linux utilities for rapid triage of large file volumes and logs:
* **Recursive Search & Filtering:** Combined use of `find` and `grep` (flags `-r`, `-n`, `-i`, `-C`, `-E`) to locate specific patterns across complex directory trees and compressed archives (`unzip -l`).
* **File & Binary Inspection:** Identifying file types regardless of extension (`file`), paginated reading (`less`), content viewing (`cat`), byte-by-byte comparison (`cmp -l`), and block-level manipulation (`dd`).
* **Terminal Encoding/Decoding:** Fast conversion and decoding of data streams using `base64 -d`, `xxd`, and `hexdump -C`.

### 2. File System & Device Management
* **Mounting & Loop Devices:** Manual creation and mounting of disk images in read-only mode (`mount -o loop,ro,offset=...`, `losetup`) for safe forensic analysis without altering data integrity.
* **Partition Diagnostics:** Calculating sector *offsets* and identifying file system structures (`ext2/3/4`, `FAT`, `NTFS`).

### 3. Shell Scripting & `.bashrc` Automation
Development of custom routines to boost productivity and monitor terminal tasks:
* **Notification Automation:** Creation of custom functions and *aliases* in `~/.bashrc` integrating visual desktop notifications (`notify-send`) and audio alerts (`paplay` / `ffmpeg`) upon completion of long-running commands.
* **Process & Subshell Management:** Running background tasks (`&`), job control, and suppressing subshell output noise.
* **Desktop Environment Autostart:** Configuring `.desktop` files in `~/.config/autostart/` for automatic startup of services and session scripts in XFCE.

### 4. Package Administration & Conflict Resolution (Arch/BlackArch)
* **Package Management with `pacman` & AUR (`yay`):** System installation, full upgrades (`pacman -Syu`), and building community packages from the Arch User Repository.
* **Dependency Troubleshooting:** Diagnosing and resolving shared library conflicts (e.g., conflicts between `libjpeg` and `libjpeg-turbo` when running tools like `steghide`).
* **Java Environment Management (JVM):** Configuring multiple OpenJDK versions (`/usr/lib/jvm/`) and resolving module incompatibilities (such as `JavaFX` and *Security Manager*) to run legacy forensic tools like Autopsy.

### 5. Hardware & System Diagnostics
* **Inventory & Monitoring:** Checking CPU architecture and hardware specifications (`lscpu`, `/proc/cpuinfo`, `inxi -C`, `lshw`) and monitoring real-time system resources and processes (`htop`, `watch`).
* **Audio Server & GUI:** Diagnosing audio subsystems (ALSA vs. PipeWire/PulseAudio) and managing/resetting desktop environments (XFCE, GNOME, KDE).
