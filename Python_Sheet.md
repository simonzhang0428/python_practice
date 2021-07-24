# Python Cheat Sheet

## Creator: [Simon Zhang](https://simonzhang0428.github.io)

## List
```python
l1 = [1, 2, 3]
l2 = [4, 5]
l1.extend(l2)
l1.pop() # default pop last element
l1.remove(2)
l1.reverse() # change in place, no return
l1.sort(min) # decresing order
l1.index(4) # first accurance
l1.count(0)
l1.sort(key=None, reverse=False) 
sorted(l1) # list not change
```

## String
```python
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
```

## Dictionary
```python
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

# f-string, concatenate string and other type
for key, value in name.items():
    print(f'{key} height: {value}')
```

## Tuple
```python
t1 = 1,
t2 = (1, 2, 3, 100, 5, 6)
t3 = tuple('hello') # ('h', 'e', 'l', 'l', 'o')
for t in t3:
    print(t)
max(t2)
sorted(t2)
len(t3)
```

## zip / enumerate
```python
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
```