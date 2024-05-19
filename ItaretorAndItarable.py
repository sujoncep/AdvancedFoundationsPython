# Iterable is an object, that one can iterate over. It generates an Iterator when passed to iter() method. An iterator is an object, which is used to iterate over an iterable object using the __next__() method.Every iterator is also an iterable, but not every iterable is an iterator in Python.

Numbers = [1, 2, 3, 4, 5]
NumbersWith = iter(Numbers)

print(next(NumbersWith))
print(next(NumbersWith))
print(next(NumbersWith))


def makeIter(n):
    preprocess = iter(n)

    while True:
        try:
            print(next(preprocess))
        except StopIteration:
            break


makeIter("Python is so powerful")
makeIter("1242424325")


class Incrementing:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count <= 100:
            x = self.count
            self.count = self.count + 1
            return x
        else:
            raise StopIteration


newObj = Incrementing()
new_iter = iter(newObj)

print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))
print(next(new_iter))

# infinite loop
for x in new_iter:
    print(x)
