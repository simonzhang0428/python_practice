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

x = "abc"
y = "def"
z = ["d", "e", "f"]
print(x.join(y)) # treat "def" as ["d", "e", "f"]
print(x.join(z))

# string.format
print("{} + {} = {}".format(3, 1, 2))
print("{one} + {two} = {three}".format(two=2, one=1, three=3))


# # %%
# msg2 = "Hello Simon"
# print(msg2)

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_[3:9]