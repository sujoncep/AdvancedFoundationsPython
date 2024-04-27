# A Python dictionary is a built-in data structure that stores key-value pairs. It's mutable, unordered, and iterable. Dictionaries are defined using curly braces {} and contain comma-separated key-value pairs in the form key: value.

# Dictionary initialization
# myDictionary = {'Name': 'john', 'age': '32'}
# print(myDictionary['Name'])
# print(myDictionary['age'])

# Dictionary modification
# myDictionary['Name']='Vector'
# print(myDictionary['Name'])

# error for no instance
# print(myDictionary['city'])

# default dictionary

from collections import defaultdict
defaultdict1 = defaultdict(set)

defaultdict1['one'].add(1)
defaultdict1['two'].add(2)
defaultdict1['three'].add(3)
defaultdict1['four']

print(dict(defaultdict1.items()))
