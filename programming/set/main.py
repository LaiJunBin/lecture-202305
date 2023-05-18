import sys


for line in sys.stdin:
    data = line.strip().split()
    a = set(data[0].split(','))
    b = set(data[1].split(','))

    print(','.join(sorted(a & b)))


