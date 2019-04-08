import sys
import re
# https://wiki.osdev.org/USB_Human_Interface_Devices

scancodes = {
    '04' : 'a',
    '05' : 'b',
    '06' : 'c',
    '07' : 'd',
    '08' : 'e',
    '09' : 'f',
    '0a' : 'g',
    '0b' : 'h',
    '0c' : 'i',
    '0d' : 'j',
    '0e' : 'k',
    '0f' : 'l',
    '10' : 'm',
    '11' : 'n',
    '12' : 'o',
    '13' : 'p',
    '14' : 'q',
    '15' : 'r',
    '16' : 's',
    '17' : 't',
    '18' : 'u',
    '19' : 'v',
    '1a' : 'w',
    '1b' : 'x',
    '1c' : 'y',
    '1d' : 'z',
    '1e' : '1',
    '1f' : '2',
    '20' : '3',
    '21' : '4',
    '22' : '5',
    '23' : '6',
    '24' : '7',
    '25' : '8',
    '26' : '9',
    '27' : '0',
    '28' : '\n',
    # '29' : '', ESC
    '2a' : '\b',
    '2b' : '\t',
    '2c' : ' ', #Space
    '2d' : '_', # Or "-"
    '2f' : '{',
    '30' : '}',
    '34' : '\'',
    '37' : '.', # or '>'
}

if len(sys.argv) != 2:
    print("[*] Usage: python scancode.py FILE_PATH")
    exit()

try:
    data = None
    with open(sys.argv[1], 'r') as file:
        data = file.readlines()
except FileNotFoundError:
    print("[*] File cannot be found!")
    exit(0)

result = [''] * 100
writePosition = 0
for line in data:
    line = line.replace(":", "")

    parts = re.findall(r"..", line)

    # Includes keys active at the time of typing like CAPS LOCK
    mode = parts[0]
    hidCode = parts[2]

    if hidCode != '00':

        # Moves the cursor left or right
        # LEFT
        if hidCode == "50":
            writePosition -= 1

        # RIGHT
        elif hidCode == "4f":
            writePosition += 1
        
        else:
            char = scancodes[hidCode]

            # Caps lock on
            if mode == "02":
                char = char.upper()

            result.insert(writePosition, char)
            writePosition += 1

print("".join(result))