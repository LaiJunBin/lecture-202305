import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

os.system('python main.py < testin > testout2')

with open('./testout', 'r') as f:
    correct = f.readlines()

with open('./testout2', 'r') as f:
    output = f.readlines()

for i in range(len(correct)):
    if correct[i] != output[i]:
        print('Test case ' + str(i + 1) + ' failed.')
        print('Expected: ' + correct[i])
        print('Got: ' + output[i])
        break

print('All test cases passed.')



