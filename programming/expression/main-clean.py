import sys

def calculate(expressions):
    while '(' in expressions:
        left = len(expressions) - expressions[::-1].index('(') - 1
        right = expressions.index(')', left)
        sub_expressions = expressions[left+1:right]
        result = calculate(sub_expressions)
        expressions = expressions[:left] + [result] + expressions[right+1:]

    while '*' in expressions or '/' in expressions:
        for i in range(1, len(expressions) - 1, 2):
            a = int(expressions[i-1])
            operator = expressions[i]
            b = int(expressions[i+1])

            if operator == '*' or operator == '/':
                c = a * b if operator == '*' else a / b
                expressions = expressions[:i-1] + [c] + expressions[i+2:]
                break

    while len(expressions) > 1:
        a = int(expressions[0])
        operator = expressions[1]
        b = int(expressions[2])

        c = a + b if operator == '+' else a - b
        expressions = [c] + expressions[3:]

    return expressions[0]

for line in sys.stdin:
    expressions = line.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
    result = calculate(expressions)
    print(result)

    
