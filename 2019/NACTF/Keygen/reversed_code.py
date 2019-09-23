import subprocess
import random
import string
import os 

possibility = string.ascii_lowercase + \
              string.ascii_uppercase + \
              "1234567890"

TARGET_VALUE = 0x1371fcaacf98

def next_round(char, calc):
    print(chr(char))
    return calc / 0x3e

for x in range(8):
    remainder = 0

    new_temp = None

    for x in range(ord("/") + 1, ord(":")):

        calc = TARGET_VALUE - x - 4
        remainder = calc % 0x3e

        if remainder == 0:
            new_temp = next_round(x, calc)

    for x in range(ord("`") + 1, ord("{")):

        calc = TARGET_VALUE - x + 0x47
        remainder = calc % 0x3e

        if remainder == 0:
            new_temp = next_round(x, calc)

    for x in range(ord("@") + 1, ord("[")):
        calc = TARGET_VALUE - x + 0x41
        remainder = calc % 0x3e

        if remainder == 0:
            new_temp = next_round(x, calc)

    if new_temp == None:
        print("[!] No value found!")
        exit()

    else:
        TARGET_VALUE = new_temp

    print()