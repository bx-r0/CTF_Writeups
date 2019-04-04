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
