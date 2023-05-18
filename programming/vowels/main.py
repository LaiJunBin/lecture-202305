import sys


for line in sys.stdin:
    s, k = line.split()
    k = int(k)

    vowels = 'aeiou'
    flags = [i in vowels for i in s]
    output = sum(flags[:int(k)])
    count = output
    l = k

    while l < len(flags):
        if flags[l]:
            count += 1

        if flags[l - k]:
            count -= 1

        output = max(count, output)
        l += 1

    print(output)

    

