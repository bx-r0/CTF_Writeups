import re

cmd = "/home/main_user/Documents/Boot2Root_CTF/Bird/"

data = None
with open(cmd + "bird.dat", 'rb') as file:
    data = file.read()

newData = [None] * len(data)

for x in range(0, len(data), 2):
    newData[x + 1], newData[x] = bytes([data[x]]), bytes([data[x + 1]])

# newData[0] = b"\xfe"
# newData[1] = b"\xca"
# newData[2] = b"\xbe"
# newData[3] = b"\xba"
flippedData = b"".join(newData)

with open(cmd + "bird_flipped.data", "wb") as file:
    file.write(flippedData)