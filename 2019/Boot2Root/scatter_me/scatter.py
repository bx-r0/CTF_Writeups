import matplotlib.pyplot as plt

data = None
with open("./scatter", 'r') as file:
    data = file.read()

points = data.split(";")

plots = []
x = []
y = []

for p in points:

    point_parts = p.split(":")
    x.append(point_parts[0])
    y.append(point_parts[1])

plt.scatter(x, y, c="r")
plt.gca().invert_yaxis()
plt.axis('off')
plt.show()

