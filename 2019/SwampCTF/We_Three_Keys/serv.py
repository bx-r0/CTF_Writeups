#!/usr/bin/env python2
from Crypto.Cipher import AES
from keys import key1, key2, key3

def pkcs7_pad(msg):
    val = 16 - (len(msg) % 16)
    if val == 0:
        val = 16
    pad_data = msg + (chr(val) * val)
    return pad_data

def encrypt_message(key, IV):
    print("What message woud you like to encrypt (in hex)?")
    ptxt = raw_input("<= ")
    ptxt = pkcs7_pad(ptxt.decode('hex'))
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ctxt = cipher.encrypt(ptxt)
    print ctxt.encode('hex')

def decrypt_message(key, IV):
    print("What message would you like to decrypt (in hex)?")
    ctxt = raw_input("<= ")
    ctxt = ctxt.decode('hex')
    if (len(ctxt) % 16) != 0:
        print "What a fake message, I see through your lies"
        return
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ptxt = cipher.decrypt(ctxt)
    print ptxt.encode('hex')

def new_key():
    print("Which key would you like to use now? All 3 are great")
    key_opt = str(raw_input("<= "))
    if key_opt == "1":
        key = key1
    elif key_opt == "2":
        key = key2
    elif key_opt == "3":
        key = key3
    else:
        print("Still no, pick a real key plz")
        exit()
    return key

def main():
    print("Hello! We present you with the future kings, we three keys!")
    print("Pick your key, and pick wisely!")
    key_opt = str(raw_input("<= "))
    if key_opt == "1":
        key = key1
    elif key_opt == "2":
        key = key2
    elif key_opt == "3":
        key = key3
    else:
        print("Come on, I said we have 3!")
        exit()
    while True:
        print("1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Choose a new key")
        print("4) Exit")
        choice = str(raw_input("<= "))
        if choice == "1":
            encrypt_message(key, key)
        elif choice == "2":
            decrypt_message(key, key)
        elif choice == "3":
            key = new_key()
        else:
            exit()


if __name__=='__main__':
    main()
