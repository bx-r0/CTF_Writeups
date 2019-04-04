data = None
with open('flag.txt', 'r') as file:
    data = file.read()

data = data.replace("-", "")
data = data.replace("dah", '-')
data = data.replace("dit", ".")
data = data.replace("di", ".")

print(data)