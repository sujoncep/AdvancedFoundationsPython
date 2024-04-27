
from collections import namedtuple
point2d = namedtuple('point2d', ['x', 'y'])
point1 = point2d(50, 100)
print(point1)
print(isinstance(point1, point2d))
print(isinstance(point1, tuple))

# unpacking tuple
x, y = point1
print(f"{x},{y}")

# index number
x = point1[0]
y = point1[1]
print(f"{x},{y}")

# iterate over point

for x in point1:
    print(x)

circle = namedtuple('circle', ['x', 'y', 'radious'], rename=True)
print(circle._fields)
