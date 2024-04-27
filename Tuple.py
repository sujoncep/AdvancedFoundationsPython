# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

firstTuple = ("apple", "banana", "orange", "cherry",
              "orange", "kiwi", "melon", "mango")
secondTuple = (1, 2, 3, 4, 5, 6)
thirdTuple = (1.2, 23.4, 24.4)
fouthTuple = (True, False)
fifthTuple = ("name", "age", True, 123)
# print(firstTuple)
# print(len(firstTuple))
# print(type(firstTuple))

# print(firstTuple[-1])
# print(firstTuple[0])
# print(firstTuple[2:6])

# check tuple

# if "apple" in firstTuple:
#     print("this fruit is avilable!")
# else:
#     print("OPPs")

# List and tuple interchange

x = list(firstTuple)
x.append("Malta")
x.remove("apple")
tuple1 = tuple(x)
print(tuple1)
