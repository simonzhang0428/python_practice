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
lst1.reverse()
lst1.sort(min) # decresing order
lst1.index(4) # first accurance
lst1.count(0)

tuple_ = (1, 2, 3 )
# TypeError: 'tuple' object does not support item assignment
# tuple_[1] = 5 
(1).__class__
(1,).__class__ # only one element need ,

# dict
name = {"Simon" : 178,
        "Helen" : 165}
name["Simon"]
name["Helen"] = 999

# f-string, concatenate string and other type
for key, value in name.items():
    print(f'{key} height: {value}')

name.get("Dudu", 30) # default value is 30
for key in name: # same as keys()
    print(key)

name.setdefault("Dudu", 30)
name.setdefault("Simon", 200) # only set when key is not in dict
name["Simon"] = 666
