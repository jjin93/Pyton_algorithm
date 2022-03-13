import sys
def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n-1)
    else:
        return 1

a = int(sys.stdin.readline())
print(my_factorial(a))


