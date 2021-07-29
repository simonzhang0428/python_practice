s = {1, 2, 3, 4, 5}
s2 = {1, 2, 6}
s.discard('0')
print(s.difference(s2))
s.difference_update(s2)
s.intersection_update(s2) # s = s & s2
s.isdisjoint(s2)
s ^ s2
s.update(s2)