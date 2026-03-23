def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))

        elif token in ["True", "False"]:
            stack.append(token == "True")

        else:
            if token == "not":
                a = stack.pop()
                stack.append(not a)
                continue

            b = stack.pop()
            a = stack.pop()

           
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

            
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

            
            elif token == 'and':
                stack.append(a and b)
            elif token == 'or':
                stack.append(a or b)

    return stack.pop()



expr = "5 3 > 2 1 < and"
print("Postfix Result:", evaluate_postfix(expr))