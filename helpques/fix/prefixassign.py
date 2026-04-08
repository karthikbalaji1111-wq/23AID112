def evaluate_prefix(expression):
    stack = []
    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ["True", "False"]:
            stack.append(token == "True")
        else:
            if token == "not":
                a = stack.pop()
                stack.append(not a)
                continue

            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

            # Comparison
            elif token == '>':
                stack.append(a > b)
            elif token == '<':
                stack.append(a < b)
            elif token == '>=':
                stack.append(a >= b)
            elif token == '<=':
                stack.append(a <= b)
            elif token == '==':
                stack.append(a == b)
            elif token == '!=':
                stack.append(a != b)

            # Logical
            elif token == 'and':
                stack.append(a and b)
            elif token == 'or':
                stack.append(a or b)

    return stack.pop()