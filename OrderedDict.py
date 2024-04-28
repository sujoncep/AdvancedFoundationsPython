# OrderedDict is a dictionary subclass provided by Python's collections module that remembers the order in which key-value pairs are inserted. In a regular dictionary, the order of insertion is not preserved, but OrderedDict maintains the insertion order, which can be useful in certain scenarios.

from collections import OrderedDict

simpleDict = {"apple": 2, "banana": 3, "orange": 4}
OrderedDict = OrderedDict(simpleDict)
# print(simpleDict)
# print(OrderedDict)

# add item
OrderedDict['fig'] = 10
print(OrderedDict)

# delete item
OrderedDict.pop('apple')
print(OrderedDict)

#reverse
for x in reversed(OrderedDict):
    print(x)