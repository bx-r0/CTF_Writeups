data = []
with open("ct.txt", 'r') as file:
    data = file.read()

data = data.replace("_", "B")
data = data.replace("-", "A")

print(data)