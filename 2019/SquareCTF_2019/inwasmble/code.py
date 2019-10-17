target = [
             3,   7,  43,  15, 211,  23, 251,  31, 163,  39, 203, 
            47, 115,  55, 155,  63,  67,  71, 107,  79,  19,  87, 
            59,  95, 227, 103,  11, 111, 179, 119, 219, 127
        ]

xor_string = b"Jj[`\xa0d\x92}\xcfB\xebF\x00\x17\xfdP1g\x1f'vwN1\x94\x0eg\x03\xda\x19\xbcQ"

for i, x in enumerate(xor_string):
    print(chr(x ^ target[i]), end="")

print()