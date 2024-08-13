# for CP

# from itertools import permutations
# print([i for i in list(permutations(arr, n))])


def fact(x):
    if x <= 1:
        return 1
    return x * fact(x - 1)


a = 0


def fib(x):
    if x <= 1:
        return x
    return fib(x - 1) + fib(x - 2)


print(fib(10))
