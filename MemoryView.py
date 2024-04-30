# memoryview is a built-in Python object that provides a view of the memory of an object. It allows you to access the internal data of an object's buffer without copying it. This can be useful when you need to access or manipulate the underlying memory of objects like bytes, bytearray, or arrays.

string = b" Python Programming "

M = memoryview(string)
print(type(string))
print(M)
print(M.obj)
print(M.tolist())

x=bytearray("python is so powerfull","utf-8")
print(type(x))
y=memoryview(x)
print(y)
print(y[4])
