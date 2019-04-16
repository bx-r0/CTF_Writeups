# key_me_baby

### Background

This task involved a pcap file containing ```USB```  packets.

The initial packets show the insertion of a keyboard:

![](./images/device.png)

With further inspection it was clear that the keys pressed were being transported by USB ```USB_INTERRUPT in``` packets

The packet contains live capture data. Using this ![resource](https://wiki.osdev.org/USB_Human_Interface_Devices) we can decode the transported data.

Each byte is reserved for a different purpose:

| Offset (Byte) | Description               |
|---------------|---------------------------|
| 0             | Modifier keys status.     |       
| 1 	        | Reserved field.           |   
| 2 	        | Keypress #1.              |
| 3 	        | Keypress #2.              |
| 4 	        | Keypress #3.              |
| 5 	        | Keypress #4.              |
| 6 	        | Keypress #5.              |
| 7 	        | Keypress #6.              | 


Therefore, this example:
```
00001c0000000000
```

Can be decoded like so:

```
Modifier = 00
Keypress #1 = 1c
```

```1c``` is the scan-code for the letter ```y```.

The modifier defined which keys were active at the time of the key press such as ```CAPS_LOCK``` or 
```SCROLL_LOCK``` etc. More information can be found at the ![resource](https://wiki.osdev.org/).

### Solution

To obtain these data points we need to extract them from the pcap we need to extract just the hid codes.
We will use a ```tshark``` command for this. The command used is below: 

```
tshark -r data.pcapng -Y "usb.transfer_type == 0x01" -T fields -e usb.capdata | awk 'NF' > keystrokes.txt
```

This grabs the ```usb.capdata``` section of the ```usb.transfer_type``` that is just the ```USB_INTERRUPT in``` packets.

A script can then be used to automate the solution. The code used is below:

```python
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
    '2a' : '\b',
    '2b' : '\t',
    '2c' : ' ', #Space
    '2d' : '_', # Or "-"
    '2f' : '{', # Or "["
    '30' : '}', # Or "]"
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

    # Checks for length
    if len(line.strip()) != 16:
        continue

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
```

The program just works as a dictionary lookup program. Running this through the keystroke.txt data it will provide the flag.

```
FLAG: b00t2root{capturethekey}
```