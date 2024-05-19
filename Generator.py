
# a generator is a special type of iterator that allows you to iterate over a sequence of values. Unlike lists or other collections, generators produce items one at a time and only when required, which makes them memory efficient.
def genaretor():
    x = 0
    print("our first point is here")
    yield x
    x += 1
    print("our secound point is here")
    yield x
    x += 1
    print("our third point is here")
    yield x
    x += 1
    print("our fourth point is here")
    yield x


obj = genaretor()

# print(f"the value of x is {next(obj)}")
# print(f"the value of x is {next(obj)}")
# print(f"the value of x is {next(obj)}")
# print(f"the value of x is {next(obj)}")

for i in obj:
    print(f"the value id x us is {i}")

list1 = [i*i for i in range(0, 12)]
generator1 = (i*i for i in range(0, 12))

print(list1)
for i in generator1:
    print(i)
