import matplotlib.pyplot as plt

data = None
with open("/home/main_user/Documents/Boot2Root_CTF/SCAT/scatter", 'r') as file:
    data = file.read()

points = data.split(";")

plots = []
for p in points:

    s = 121
    point_parts = p.split(":")
    plt.scatter(x=point_parts[1], y=point_parts[0], c="r")

plt.show()

