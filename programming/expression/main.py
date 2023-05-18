import sys

for line in sys.stdin:
    expressions = line.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()

    while '(' in expressions:
        left = len(expressions) - expressions[::-1].index('(') - 1
        right = expressions.index(')', left)
        sub_expressions = expressions[left+1:right]

        while '*' in sub_expressions or '/' in sub_expressions:
            for i in range(1, len(sub_expressions) - 1, 2):
                a = int(sub_expressions[i-1])
                operator = sub_expressions[i]
                b = int(sub_expressions[i+1])

                if operator == '*' or operator == '/':
                    c = a * b if operator == '*' else a / b
                    sub_expressions = sub_expressions[:i-1] + [c] + sub_expressions[i+2:]
                    break

        while len(sub_expressions) > 1:
            a = int(sub_expressions[0])
            operator = sub_expressions[1]
            b = int(sub_expressions[2])

            c = a + b if operator == '+' else a - b
            sub_expressions = [c] + sub_expressions[3:]

        result = sub_expressions[0]
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

    print(expressions[0])

    
