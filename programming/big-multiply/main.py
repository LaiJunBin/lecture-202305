import sys


for line in sys.stdin:
    a, b = [[int(num) for num in i] for i in line.strip().split()]
    c = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            c[i + j + 1] += a[i] * b[j]
            if c[i + j + 1] > 9:
                c[i + j] += c[i + j + 1] // 10
                c[i + j + 1] %= 10

    print(''.join([str(i) for i in c]).lstrip('0'))        
