from collections import Counter

list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))

s = 'simon zhang'
Counter(s)

dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
Counter(dict1)

tuple1 = ('x','y','z','x','x','x','y', 'z')
Counter(tuple1) # return dict

c = Counter()
c.update('sssssimonnnnn')
print(c)

for ch in c:
    print(f'{ch} : {c[ch]}')

del c['s']

counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})
counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })

#Addition
counter3 = counter1 + counter2 
# only the values that are positive will be returned.
print(counter3)

#Subtraction
counter4 = counter1 - counter2 
# all negative numbers are excluded.
# For example z will be z = -2-4=-6, since it is negative value it is not shown in the output
print(counter4)

#Intersection
counter5 = counter1 & counter2 # it will give all common positive minimum values from counter1 and counter2
print(counter5)

#Union
counter6 = counter1 | counter2 # it will give positive max values from counter1 and counter2
print(counter6)


counter1 =  Counter({'x': 5, 'y': 2, 'z': -2, 'x1':0})
_elements = counter1.elements() # will give you all elements with positive value and count>0
for a in _elements: # tertools.chain object
    print(a)
counter1.most_common() # default sort and return all
counter1.subtract(counter2) # c1 - c2
counter1.update(counter2) # c1 + c2