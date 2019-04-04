# ham-me-baby
This challenge involved fixing Hamming(7,4) values to receive the flag

Below is the prompt for the netcat server:
```

                        Welcome To 

     ____                       __    _______________  
    / __/__  __________ _____  / /_  / ___/_  __/ __/  
   / _// _ \/ __/ __/ // / _ \/ __/ / /__  / / / _/    
  /___/_//_/\__/_/  \_, / .__/\__/  \___/ /_/ /_/      
                ___/___/_/_____                        
               |_  |/ _ <  / _ \                       
              / __// // / /\_, /                       
             /____/\___/_//___/                        
                                                         

you will be receiving hamming(7,4) codes. your job is to send data bits
from a 7 bit hamming code. 
 ___________________________________________________________________
|                                                                   |
|   DO YOUR RESEARCH : https://en.wikipedia.org/wiki/Hamming(7,4)   |
|  FLAG WILL BE PRINTED AFTER YOU SEND CORRECT DATA BITS 100 TIMES  |
|___________________________________________________________________|

               the order of the bits followed is

                    P1 P2 D3 P4 D5 D6 D7


and come back here. remember somebits could be flipped. you need to send
correct data bits.

[*] CODE: 0101010
[*] DATA: 
```

This involved dynamically taking values and returning the 4 bits of data. 

Hamming(7,4) works by having 3 parity bits for 4 bit of data.

```
P1 P2 D3 P4 D5 D6 D7
0  1  0  1  0  1  0
```

This value is split into 3 parity sets:

Parity 1:
```
P1 D3 D5 D7
0  0  0  0
```

Parity 2:
```
P2 D3 D6 D7
1  0  1  0
```

Parity 3:
```
P4 D5 D6 D7
1  0  1  0
````

Errors in these sets will tell us which value is incorrect and allow us to fix it

For example:
If the error is in ```D3``` we would have errors in ```Parity 1``` and ```Parity 2```. This is the only combination that would give us this error. If we flip D3 we have the correct data value.

Below is the solution to the completed challenge:

```python
from pwn import *
import numpy as np

def even_check(value):
    
    count = 0
    for c in value:
        if c == '1':
            count += 1

    return count % 2 == 0

def flip(bit):
    if bit == '0':
        return '1'
    else:
        return '0'

def hamming(code):
    code_list = np.array(list(code))

    # 1,3,5,7
    p1 = code_list[[0,2,4,6]]
    p1_check = even_check(p1)

    # 2,3,6,7
    p2 = code_list[[1,2,5,6]]
    p2_check = even_check(p2)

    # 4,5,6,7
    p3 = code_list[[3,4,5,6]]
    p3_check = even_check(p3)

    # Err: 3
    if (not p1_check and not p2_check) and p3_check:
        code_list[2] = flip(code_list[2])

    # Err: 5
    elif (not p1_check and not p3_check) and p2_check:
        code_list[4] = flip(code_list[4])

    # Err: 6
    elif (not p2_check and not p3_check) and p1_check:
        code_list[5] = flip(code_list[5])

    # Err: 7
    elif not p2_check and not p3_check and not p1_check:
        code_list[6] = flip(code_list[6])

    # Returns the data bits
    return "".join(code_list[[2,4,5,6]])


r = remote("104.154.106.182", 6969)
r.recvuntil("CODE: ")
code = ""

for x in range(100):
    if not "Invalid" or not "Wrong" in code:
        print(f"CODE: {x}")
        code = r.read().decode("utf-8")[:7]
        response = hamming(code)
        r.send(response + "\n")

        if x != 99:
            r.recvuntil("CODE: ")
        else:
            # Flag?
            print(r.read().decode("utf-8"))
    else:
        print("INVALID")
        print(f"Last response: {response}")
        break
```

```FLAG: encryptCTF{1t_w4s_h4rd3r_th4n_1_th0ught}```