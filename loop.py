for i in range(4):
    print(i)

num = 10
while num >= 5:
    print(num)
    num -= 1

list(range(10))

a = [1, 2, 3]
b = ['Simon', 'Helen', 'Dudu']
for i in zip(a, b):
    print(i)

from math import sqrt
for n in range(82,100):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

else:
    print("Don't find!")

