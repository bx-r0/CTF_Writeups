# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.4+ (default, Sep  4 2019, 08:03:05) 
# [GCC 9.2.1 20190827]
# Embedded file name: ./encoder.py
# Compiled at: 2019-10-10 01:14:05
import base64, string, sys
from random import shuffle

def encode(f, inp):
    s = string.printable
    init = lambda : (list(s), [])
    bag, buf = init()

    for x in inp:
        if x not in s:
            continue
        while True:
            r = bag[0]
            bag.remove(r)
            diff = (ord(x) - ord(r) + len(s)) % len(s)
            if diff == 0 or len(bag) == 0:
                shuffle(buf)
                f.write(str.encode(('').join(buf)))
                f.write(b'\x00')
                bag, buf = init()
                shuffle(bag)
            else:
                break

        buf.extend(r * (diff - 1))
        f.write(str.encode(r))

    shuffle(buf)
    f.write(str.encode(('').join(buf)))

if __name__ == '__main__':

    fileName = "desc.txt"

    with open(fileName, 'rb') as (r):
        w = open(fileName + '.enc', 'wb')
        b64 = base64.b64encode(r.read()).decode("utf-8")
        encode(w, b64)
# okay decompiling ../decodeme/encoder.pyc