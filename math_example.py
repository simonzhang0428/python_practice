import math

math.isclose(1, 1.000000)
math.sqrt(4)
math.pi
math.exp(2)

good_style = True
snake_case = good_style

l = list(range(10))
l2 = [4, 3, 2, 1]
l2.sort()
l2
l3 = [4, 3, 2, 1]
sorted(l3) # not modify l3, return new copy

def powerof(num):
    return num, num ** 2, num ** 3

# tuple unpacking
x, y, z = powerof(3)
x, y, z