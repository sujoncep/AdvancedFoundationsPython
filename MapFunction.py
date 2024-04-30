# A mapping object in Python is any object that implements the mapping protocol, meaning it provides a way to map keys to values. The most common example of a mapping object in Python is the dictionary(dict) data type. Mapping objects are collections of key-value pairs where each key is associated with a value. They are iterable and allow for quick lookups based on keys.
newList = [10, 20, 30, 40]


def addition(n):
    return n+5


myList = map(addition, newList)
print(myList)

for x in myList:
    print(x)


def adding(x, y):
    return x+y


myList1 = map(adding, ('apple', 'watermolen'), ('banana', 'fig'))
print(tuple(myList1))

number1 = [10, 20, 30, 40]
number2 = [2, 3, 4, 5]
newResult = map(lambda a, b: a*b, number1, number2)
print(list(newResult))
