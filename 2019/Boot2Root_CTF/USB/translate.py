#!/usr/bin/python
#coding=utf-8
import os, operator, sys

# newmap = { 1: "",
#  2: “PostFail”,
#  3: "",
#  4: “a”,
#  5: “b”,
#  6: “c”,
#  7: “d”,
#  8: “e”,
#  9: “f”,
#  10: “g”,
#  11: “h”,
#  12: “i”,
#  13: “j”,
#  14: “k”,
#  15: “l”,
#  16: “m”,
#  17: “n”,
#  18: “o”,
#  19: “p”,
#  20: “q”,
#  21: “r”,
#  22: “s”,
#  23: “t”,
#  24: “u”,
#  25: “v”,
#  26: “w”,
#  27: “x”,
#  28: “y”,
#  29: “z”,
#  30: “1”,
#  31: “2”,
#  32: “3”,
#  33: “4”,
#  34: “5”,
#  35: “6”,
#  36: “7”,
#  37: “8”,
#  38: “9”,
#  39: “0”,
#  40: “Enter”,
#  41: “esc”,
#  42: “del”,
#  43: “tab”,
#  44: “space”,
#  45: “-”,
#  47: “[“,
#  48: “]”,
#  56: “/”,
#  57: “CapsLock”,
#  79: “RightArrow”,
#  80: “LetfArrow”
#  }

newmap = {
    # 2: "PostFail",
    4: "a",
    5: "b",
    6: "c",
    7: "d",
    8: "e",
    9: "f",
    10: "g",
    11: "h",
    12: "i",
	13: "j",
    14: "k",
    15: "l",
    16: "m",
    17: "n",
    18: "o",
    19: "p",
    20: "q",
    21: 'r',
    22: 's',
    23: 't',
    24: 'u',
    25: 'v',
    26: 'w',
    27: 'x',
    28: 'y',
    29: 'z',
    30: '1',
    31: '2',
    32: '3',
    33: '4',
    34: '5',
    35: '6',
    36: '7',
    37: '8',
    38: '9',
    39: '0',
    40: '\r\n',
    41: 'ESC',
    42: "del",
    43: 'tab',
    44: 'space',
    45: '-',
    47: '[',
    48: ']',
    55: '*',
    56: '/',
    57: 'CapsLock',
    79: '>',
    80: '<'
}
message = ""
myKeys = open("keystrokes.txt")
i = 1
for line in myKeys:
    # print line
    bytesArray = bytearray.fromhex(line.strip())
    # print "BytesArray = ", str(bytesArray)
    for byte in bytesArray:
        if byte != 0:
            print "Debug Byte = ", str(byte) 
            keyVal = int(byte)

            if keyVal in newmap:
                print newmap[keyVal]
                message += newmap[keyVal]
                # message.append(newmap[keyVal])
                print "DEBUG Key Value: ", str(keyVal), "Equals: ", str(newmap[keyVal])
                print message
            else:
                pass
                print "\r\nNo map found for this value: " + str(keyVal)
            i += 1

 # #print format(byte, ‘02X’)
 # i+=1
