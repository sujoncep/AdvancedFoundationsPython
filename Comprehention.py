# List Comprehension
# List comprehension is a concise way of creating lists in Python. It allows you to define a list by specifying an expression, usually involving the elements of an iterable, followed by a loop and optional conditional statements.

# regular way

FruitList = ['banan', 'cherry', 'apple']
mylist = []

for item in FruitList:
    if "a" in item:
        mylist.append(item)

print(mylist)

# Use list Comprehension
FruitList = ['banan', 'cherry', 'apple']
mylist = [item for item in FruitList if "a" in item]
