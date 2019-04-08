# Scatter Me

![](./brief.png)


We are initially provided with a file ```scatter```:
```
1:3:1;1.25:3:1;1.5:3:1;1.75:3:1;2:3:1;2:2.75:1;2:2.5:1;2:2.25:1;2:2:1;2:1.75:1;2:1.5:1;1:2.25:1;1.25:2.25:1;1.5:2.25:1;1.75:2.25:1;1:1.5:1;1.25:1.5:1;1.5:1.5:1;1.75:1.5:1;3:3:1;3.25:3:1;3.5:3:1;3.75:3:1;4:3:1;4:2.75:1;4:2.5:1;4:2.25:1;4:2:1;4:1.75:1;4:1.5:1;3:1.5:1;3.25:1.5:1;3.5:1.5:1;3.75:1.5:1;3:1.75:1;3:2:1;3:2.25:1;3:2.5:1;3:2.75:1;5:3:1;5.25:3:1;5.5:3:1;5.75:3:1;6:3:1;6:2.75:1;6:2.5:1;6:2.25:1;6:2:1;6:1.75:1;6:1.5:1;5.75:1.5:1;5.5:1.5:1;5.25:1.5:1;5:1.5:1;5:1.75:1;5:2:1;5:2.25:1;5:2.5:1;5:2.75:1;7:3:1;7.25:3:1;7.5:3:1;7.75:3:1;8:3:1;8:2.75:1;8:2.5:1;8:2.25:1;8:2:1;8:1.75:1;8:1.5:1;9:3:1;9.25:3:1;9.5:3:1;9.75:3:1;10:3:1;10:2.75:1;10:2.5:1;10:2.25:1;9.75:2.25:1;9.5:2.25:1;9.25:2.25:1;9:2.25:1;9:2:1;9:1.75:1;9:1.5:1;9.25:1.5:1;9.5:1.5:1;9.75:1.5:1;10:1.5:1;11:3:1;11.25:3:1;11.5:3:1;11.75:3:1;12:3:1;12:2.75:1;12:2.5:1;12:2.25:1;12:2:1;12:1.75:1;12:1.5:1;11.75:1.5:1;11.5:1.5:1;11.25:1.5:1;11:1.5:1;11:1.75:1;11:2:1;11:2.25:1;11:2.5:1;11:2.75:1;11.25:2.25:1;11.5:2.25:1;11.75:2.25:1
```

After looking at the pattern of the text file it can be seen that the pattern follows 3 numbers and a semi colon separator.

The next step was splitting the values into x, y and z. Though z can be ignored due to it never being different from 1.

Below is the python code used:

```python
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
```

This uses ```matplotlib``` to take the values and produce a graph. Initially the y-axis and provided us with an inaccurate value. Flipping off the y-axis was achieved with this line:

```python
plt.gca().invert_yaxis()
```

The output of the script is below:

![](./flag.png)

This pincode was then used to create the flag

```
FLAG: b00t2root{300728}
```