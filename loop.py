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

key = 'abc'
value = '123'
for pair in zip(key, value):
    print(pair)

list(enumerate('simon')) # [(0, 's'), (1, 'i'), (2, 'm'), (3, 'o'), (4, 'n')]
list(zip(range(5), 'simon'))
d = dict(enumerate('abc')) # {0: 'a', 1: 'b', 2: 'c'}
z = zip('xyz', [23, 24, 25])
dict(z)
d1 = {(0, 0) : 5}