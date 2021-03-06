lst = [1, 2, 3]
del lst[1] # O(n)
lst[1:] = [5, 6, 7, 8]
lst.append(100)
lst.append([200, 500])
len(lst)
lst.insert(0, 999) # O(n)

lst1 = [1, 2, 3]
lst2 = [4, 5]
lst1.extend(lst2)
lst1.pop() # default pop last element
lst1.remove(2)
lst1.reverse() # change in place, no return
lst1.sort(min) # decresing order
lst1.index(4) # first accurance
lst1.count(0)
lst1.sort(key=None, reverse=False) 
sorted(lst1)

tuple_ = (1, 2, 3 )
# TypeError: 'tuple' object does not support item assignment
# tuple_[1] = 5 
(1).__class__
(1,).__class__ # only one element need ,

# dict
name = {'Simom' : 178,
        'Helen' : 165}
name['Simom']
name['Helen'] = 999
name['xxx'] # KeyError
name.get('xxx') # return None
name.get('Dudu', 30) # default value is 30
for key in name: # same as keys()
    print(key)
name['GuaiGuai'] = 25 # add / modify dict use dict[key] = value
del name['GuaiGuai']
name.pop('Helen') # return value, remove entry
name.setdefault('Dudu', 30) # only set when key is not in dict
name.keys()
name.values()
name.items()
name.popitem()

# f-string, concatenate string and other type
for key, value in name.items():
    print(f'{key} height: {value}')

[i ** 2 for i in range(10)]
[i ** 2 for i in range(10) if i % 2 == 0]
[
    i ** 3 
    for i in range(10)
    if i % 2 == 0
]

names = ["simon", "helen"]
ages = [35, 36]
{name : age for name, age in zip(names, ages)}

# set
s = {c for c in 'abracaabroa' if c not in 'abc'} # {'r', 'o'}
s2 = set('foobar') # {'r', 'f', 'b', 'a', 'o'}
s3 = set(['a', 'b', 'foo'])
s.isdisjoint(s2)
s.issubset(s2)
s < s2
s.union(s2)
s.intersection(s2)
s2.difference(s) # s2 - s
s.symmetric_difference(s2) # either in s or s2, but not both