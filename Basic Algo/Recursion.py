# Find somme subtask that it can perform without calling itself, that's the basecase

def factorial(n):
    if n < 2:
        return n
    return n * factorial(n-1) 

print(factorial(5))