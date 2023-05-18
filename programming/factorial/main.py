import sys


def get_factorial(n):
    if n == 0:
        return 1

    return n * get_factorial(n - 1)

def get_factorial_with_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

for line in sys.stdin:
    n = int(line)

    print(get_factorial(n))
    print(get_factorial_with_loop(n))
