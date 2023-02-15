def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def operator_priority(operator):
    if operator in ["+", "-"]:
        return 1
    elif operator in ["*", "/", "%"]:
        return 2
    elif operator == "^":
        return 3
    elif operator == ")":
        return 4
    elif operator == "(":
        return 0

expression = "5 * ( 6 + 2 ) - 12 / 4"
tokens = expression.split()
stack = []
postfix = []
index = 1

tokens.insert(0, '(')
tokens.append(')')
stack.append('(')

while index < len(tokens):
    if is_numeric(tokens[index]):
        postfix.append(float(tokens[index]))
    elif operator_priority(tokens[index]) == 4:
        while operator_priority(stack[-1]) > 0:
            postfix.append(stack.pop())
        stack.pop()
    elif operator_priority(tokens[index]) >= operator_priority(stack[-1]) or operator_priority(tokens[index]) == 0:
        stack.append(tokens[index])
    else:
        postfix.append(stack.pop())
        stack.append(tokens[index])
    index += 1

print(postfix)
print(stack)