# for CP

# from itertools import permutations
# print([i for i in list(permutations(arr, n))])


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)
