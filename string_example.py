"""
This is comment / annotation
"""

seq = ("H", "e", "l", "l", "o")
s1 = "-"
print(s1.join(seq))

s2 = ""
print(s2.join(seq))

msg = "Simon Zhang"
print(msg)
msg.index("x") # index: throw ValueError
msg.find("x") # find: -1 if not find

x = "abc"
y = "def"
z = ["d", "e", "f"]
print(x.join(y)) # treat "def" as ["d", "e", "f"]
print(x.join(z))

# string.format
print("{} + {} = {}".format(3, 1, 2))
print("{one} + {two} = {three}".format(two=2, one=1, three=3))
print(f'message = {msg}')

# string method
s = 'hello simon'
s.title() # 'Hello Simon'
len(s)
s[5:10]
s[-3:-1]
s.upper()
s.lower()
s.index('h')
s[0] == 'h'
s = '    Haha,   SSSimonnnnn   '
s.strip()
s.strip().split(',')
s.count('S')
s.find('XX') # -1 if not find
s.index('S') # throw error if not find

# # %%
# msg2 = "Hello Simon"
# print(msg2)

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_[3:9]
list_[10:2:-1]

list2_ = ["hello", "simon"]
tuple_ = ("hey", "helen")
list_ + list2_

# error, same container needed
# list2_ + tuple_ 

list2_ * 2 # init new sequency

# shallow copy
a = [[0]]
b = a * 4
b
a = [[1]]
b
b[0][0] = 1
b

# deep copy
c = [[0] for _ in range(4)]
c


