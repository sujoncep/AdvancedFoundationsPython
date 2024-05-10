# The enumerate() function in Python is a built-in function that allows you to loop over an iterable(such as a list, tuple, or string) while also keeping track of the index of each item. It returns an enumerate object, which yields pairs containing the index and the corresponding item from the iterable.


names = ['ahmad', 'ibra', 'ira', 'jaman']

# enum = enumerate(names)
enum = enumerate(names, start=1000)
print(type(names))
print(list(enum))

# for index, name in enumerate(names):
#     print(f"Index= {index}, Name={name}")


for index, name in enumerate(names, start=1000):
    print(f"Index= {index}, Name={name}")

enum1 = enumerate(names)
print(enum1.__next__())
