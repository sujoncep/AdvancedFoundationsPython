# Counter is another handy tool provided by Python's collections module. It's a subclass of dict that allows you to count the occurrences of elements in an iterable(such as a list or a string).

from collections import Counter
newList = ['a', 's', 'w', 'f', 'y', 'g', 'a',
           's', 'w', 'f', 'a', 's', 'w', 'f', 'y', 'g']
string = ("Hi there. How are you?")

firstTuple = ("apple", "banana", "orange", "cherry",
              "orange", "kiwi", "melon", "mango", "apple", "banana", "orange", "cherry", "apple", "banana", "orange", "cherry", "apple", "banana", "orange", "cherry",
              "orange", "kiwi", "melon", "mango", "apple", "banana", "orange", "cherry", "apple", "banana", "orange", "cherry")
# print(Counter(newList))
# print(Counter(string))
print(Counter(firstTuple))