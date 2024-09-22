# Find somme subtask that it can perform without calling itself, that's the basecase

def factorial(n):
    if n < 2:
        return n
    return n * factorial(n-1) 

n = int(input())
def solve(x):
    if x == 0:
        return
    solve(x-1)
    print(x)
solve(n)




def test_all():
    print(factorial(5))