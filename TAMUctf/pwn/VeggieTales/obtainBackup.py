from pwn import *
import base64
import time
import re

r = remote("pwn.tamuctf.com", 8448)

def Read(r):
    print(r.read().decode('utf-8'))

def getEpisodeBackup(episodeList):

    for e in episodeList:

        r.read()
        r.send("1\n") # Add episode
        r.read()
        r.send(f"{e}\n") # Episode number
        time.sleep(1)
    
        print(".", end="")

    r.read()
    r.send("3\n")  # Show backup

    backupStr = r.read().decode("utf-8")

    backupStrParts = backupStr.split(":")
    backupStrParts = backupStrParts[1].split("\n")
    base64String = backupStrParts[0]

    return base64.b64decode(base64String).hex()

backupString = getEpisodeBackup(range(1, 48))
r.interactive()