import os 
import random

os.chdir(os.path.dirname(os.path.realpath(__file__)))

test_case_count = 100
test_cases = []

for i in range(test_case_count):
    a = random.randint(0, 1000000000000000000)
    b = random.randint(0, 1000000000000000000)
    test_cases.append((a, b))

with open('./testin', 'w') as f:
    for case in test_cases:
        f.write(str(case[0]) + ' ' + str(case[1]) + '\n')

with open('./testout', 'w') as f:
    for case in test_cases:
        f.write(str(case[0] * case[1]) + '\n')


