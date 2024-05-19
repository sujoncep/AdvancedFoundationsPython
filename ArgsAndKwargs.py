# *args is used to pass a variable number of positional arguments to a function. It collects all the positional arguments passed to the function into a tuple. The asterisk(*) before args denotes that it can accept multiple positional arguments.

# **kwargs is used to pass a variable number of keyword arguments to a function. It collects all the keyword arguments passed to the function into a dictionary, where the keys are the argument names and the values are the argument values. The double asterisks(**) before kwargs denotes that it can accept multiple keyword arguments.


def argsFunction(*args):
    for arg in args:
        print(arg)


argsFunction(11, 22, 33)
argsFunction('a', 'b', 'c', 'd')


def kwargesFunction(**kwarges):
    for key, value in kwarges.items():
        print(f"key={key} and value={value}")


# def argesAndKwargsFunction(*arges, **kwarges):
#     for arg in args:
#         print(arg)

#     for key, value in kwarges.items():
#         print(f"key={key} and value={value}".format(key, value))


# argesAndKwargsFunction(1, 23, 4, 53, 53, name='alice', age=20)

def argesAndKwargsFunction(*args, **kwargs):
    # You can choose to use args and kwargs as needed
    # For demonstration purposes, we'll just print them here
    for arg in args:
        print("Positional argument:", arg)

    for key, value in kwargs.items():
        print(f"Keyword argument - {key}: {value}")


# Call the function with both positional and keyword arguments
argesAndKwargsFunction(1, 23, 4, 53, 53, name='alice', age=20)
