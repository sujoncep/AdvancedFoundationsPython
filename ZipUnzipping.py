# Zipping and unzipping in Python refer to operations involving combining or separating multiple iterables(such as lists, tuples, or strings) into one or vice versa.

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
zipped = zip(list1, list2)

print(list(zipped))
for x in zip([1, 2, 3], ['x', 'y', 'z'], ['a', 'b', 'c']):
    print(x)

x = zip([10, 20], ['samir', 'pamir', 'kamir'])

y = zip([10, 20, 30], ['samir', 'pamir'])

print(list(x))
print(list(y))

# unzippping
unzipped = zip([1, 2, 3], ['x', 'y', 'z'])
a, b = zip(*unzipped)
print(a, b)

# l1, l2 = zip(*zipped)
# print(l1, l2)
