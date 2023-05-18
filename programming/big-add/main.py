import sys


for line in sys.stdin:
    a, b = [[int(num) for num in i] for i in line.strip().split()]
    # or 
    # a, b = line.strip().split()
    # a = [int(i) for i in a]
    # b = [int(i) for i in b]

    c = [0] * (max(len(a), len(b)) + 1)

    while len(a) < len(c):
        a.insert(0, 0)

    while len(b) < len(c):
        b.insert(0, 0)

    for i in range(len(c) - 1, -1, -1):
        c[i] += a[i] + b[i]
        if c[i] > 9:
            c[i] -= 10
            c[i - 1] += 1

    print(''.join([str(i) for i in c]).lstrip('0'))
    
