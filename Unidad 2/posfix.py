def operaciones(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    
def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def importancia(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/" or op == "%":
        return 2
    elif op == "^":
        return 3
    elif op == ")":
        return 4
    elif op == "(":
        return 0

def infix_to_postfix(infix_expression):
    postfix_expression = []
    stack = []
    infix_expression.insert(0,'(')
    infix_expression.append(')')
    stack.append('(')
    for i in range(1, len(infix_expression)):
        if isNumeric(infix_expression[i]):
            postfix_expression.append(float(infix_expression[i])) 
        elif importancia(infix_expression[i]) == 4:
            while importancia(stack[-1]) > 0:
                postfix_expression.append(stack.pop())
            stack.pop()
        elif importancia(infix_expression[i]) >= importancia(stack[-1]) or importancia(infix_expression[i]) == 0:
            stack.append(infix_expression[i])
        else:
            postfix_expression.append(stack.pop())
            stack.append(infix_expression[i])
    return postfix_expression

Q = "5 * ( 6 + 2 ) - 12 / 4"
p = Q.split()
postfix_expression = infix_to_postfix(p)

h = 0
while len(postfix_expression) > 1:
    h = h % len(postfix_expression)
    if type(postfix_expression[h]) is str:
        op = postfix_expression.pop(h)
        n2 = postfix_expression.pop(h - 1)
        n1 = postfix_expression.pop(h - 2)
        h -= 2
        postfix_expression.insert(h, operaciones(n1, n2, op))
    h += 1

print(postfix_expression)