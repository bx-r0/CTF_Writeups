import string
import base64

PRINTABLE_CHARS = list(string.printable)
BASE64_CHARS = f"{string.ascii_uppercase}{string.ascii_lowercase}0123456789+/="

def decode(section):
    
    recovered_string = ""

    # Find output for r
    seen = []
    r_output = ""

    for s in section:

        if s in seen:
            break
        else:
            seen.append(s)
            r_output += s

    # Grabs the remaining part of the section
    data_output = section[len(r_output):]

    # Counts the number of character occurance
    char_count = {}
    for u in set(list(data_output)):
        char_count.update({u : data_output.count(u)})

    # Loops around the r_output
    for r in r_output:

        if r not in char_count:
            diff = 1
        else:
            diff = char_count[r] + 1

        x = (diff + ord(r)) % 100

        if chr(x) not in BASE64_CHARS:
            recovered_string += chr(x + 100)
        else:
            recovered_string += chr(x)

    return recovered_string

if __name__ == "__main__": 
    
    data = b""
    with open("decodeme.png.enc", "rb") as file:
        data = file.read()

    sections = data.split(b"\x00")

    b64_data = ""

    for s in sections:
        b64_data += decode(s.decode("utf-8"))

    with open("decodeme.png", "wb") as file:
        file.write(base64.b64decode(b64_data))

    print("File decrypted!")