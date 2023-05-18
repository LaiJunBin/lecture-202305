import sys
from collections import Counter


for line in sys.stdin:
    a, b = line.strip().split()
    a = Counter(a)
    b = Counter(b)

    if a == b:
        print('True')
    else:
        print('False')

