import sys



def get_factors_with_effiently(n):
    factors = []
    
    for x in range(1, int(n**0.5)+1):
        if n % x == 0:
            factors.append(x)
            if x != n // x:
                factors.append(n // x)
    
    return factors

def get_factors(n):
    factors = []
    
    for x in range(1, n+1):
        if n % x == 0:
            factors.append(x)
    
    return factors

for line in sys.stdin:
    n = int(line)

    factors = get_factors_with_effiently(n)
    factors.sort()
    print(len(factors), factors)

