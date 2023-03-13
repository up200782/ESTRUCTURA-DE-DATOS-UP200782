import math
from tkinter import *

# Definimos una función para convertir la expresión infix a postfix
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,
                  '(': 0, 'sin': 4, 'cos': 4, 'tan': 4, 'log': 4, 'asin' : 4, 'acos': 4, 'atan':4}
    stack = []
    postfix = []
    for token in expression.split():
        if token.replace('.','',1).isdigit() or (token.startswith('-') and token[1:].replace('.','',1).isdigit()):
            postfix.append(token)
        elif token in precedence.keys():
            while stack and precedence[token] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)

# Definimos una función para evaluar la expresión en postfix
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.replace('.','',1).isdigit() or (token.startswith('-') and token[1:].replace('.','',1).isdigit()):
            stack.append(float(token))
        elif token in ['+', '-', '*', '/', '^',]:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
            stack.append(result)
        elif token in ['sin', 'cos', 'tan', 'log', 'asin', 'acos', 'atan']:
            if token == 'sin':
                operand1 = stack.pop()
                operand1 = math.radians(operand1)
                result = math.sin(operand1)
            elif token == 'cos':
                operand1 = stack.pop()
                operand1 = math.radians(operand1)
                result = math.cos(operand1)
            elif token == 'tan':
                operand1 = stack.pop()
                operand1 = math.radians(operand1)
                result = math.tan(operand1)
            elif token == 'log':
                operand1 = stack.pop()
                result = math.log(operand1)
            elif token == 'asin':
              operand1 = stack.pop()
              result = math.asin(operand1)
              result = math.degrees(result)
            elif token == 'acos':
              operand1 = stack.pop()
              result = math.acos(operand1)
              result = math.degrees(result)
            elif token == 'atan':
              operand1 = stack.pop()
              result = math.atan(operand1)
              result = math.degrees(result)
            stack.append(result)
    return stack.pop()

# Definimos una función para manejar el evento de presionar el botón "Calcular"
def calculate():
    expression = infix_to_postfix(entry.get())
    result = evaluate_postfix(expression)
    label.config(text=str(result))

# Creamos la ventana de la calculadora
window = Tk()
window.title("Calculadora")
window.geometry("300x200")

# Creamos un campo de entrada para ingresar la expresión
entry = Entry(window)
entry.pack(pady=10)
# Creamos un botón para calcular el resultado
button = Button(window, text="Calcular", command=calculate)
button.pack(pady=10)

# Creamos una etiqueta para mostrar el resultado
label = Label(window, text="")
label.pack()

# Iniciamos el bucle de eventos de la ventana
window.mainloop()

