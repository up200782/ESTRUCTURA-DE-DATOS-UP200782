import math
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Definimos una función para convertir la expresión infix a postfix


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3,
                  '(': 0, 'sin': 4, 'cos': 4, 'tan': 4, 'log': 4, 'asin': 4, 'acos': 4, 'atan': 4}
    stack = []
    postfix = []
    for token in expression.split():
        if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
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
        if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
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
# Funcion para que imprima los valores


def imprimir(valor):
    tecla.set(tecla.get() + valor)
    print(tecla.get())

# Definimos una función para manejar el evento de presionar el botón "Calcular"


def calculate():
    expression = infix_to_postfix(entry.get())
    result = evaluate_postfix(expression)
    entry.delete(0, tk.END)
    entry.insert(0, (result))


# Creamos la ventana de la calculadora
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(width=400, height=500)  # Toda la calculadora

tecla = tk.StringVar()
entry = ttk.Entry(ventana, textvariable=tecla)
entry.pack()
entry.place(x=35, y=35, width=325, height=40)  # El cuadro

button_expresion = ttk.Button(text="=", command=calculate)
button_expresion.place(x=310, y=450, width=65, height=40)
button_expresion = ttk.Button(text="0", command=lambda: imprimir("0"))
button_expresion.place(x=170, y=400, width=65, height=40)
button_expresion = ttk.Button(text="1", command=lambda: imprimir("1"))
button_expresion.place(x=100, y=400, width=65, height=40)
button_expresion = ttk.Button(text="2", command=lambda: imprimir("2"))
button_expresion.place(x=30, y=400, width=65, height=40)
button_expresion = ttk.Button(text="3", command=lambda: imprimir("3"))
button_expresion.place(x=240, y=350, width=65, height=40)
button_expresion = ttk.Button(text="4", command=lambda: imprimir("4"))
button_expresion.place(x=170, y=350, width=65, height=40)
button_expresion = ttk.Button(text="5", command=lambda: imprimir("5"))
button_expresion.place(x=100, y=350, width=65, height=40)
button_expresion = ttk.Button(text="6", command=lambda: imprimir("6"))
button_expresion.place(x=30, y=350, width=65, height=40)
button_expresion = ttk.Button(text="7", command=lambda: imprimir("7"))
button_expresion.place(x=30, y=300, width=65, height=40)
button_expresion = ttk.Button(text="8", command=lambda: imprimir("8"))
button_expresion.place(x=100, y=300, width=65, height=40)
button_expresion = ttk.Button(text="9", command=lambda: imprimir("9"))
button_expresion.place(x=170, y=300, width=65, height=40)
button_expresion = ttk.Button(text="+", command=lambda: imprimir("+"))
button_expresion.place(x=240, y=300, width=65, height=40)
button_expresion = ttk.Button(text="-", command=lambda: imprimir("-"))
button_expresion.place(x=240, y=400, width=65, height=40)
button_expresion = ttk.Button(text="*", command=lambda: imprimir("*"))
button_expresion.place(x=310, y=300, width=65, height=40)
button_expresion = ttk.Button(text="/", command=lambda: imprimir("/"))
button_expresion.place(x=310, y=350, width=65, height=40)
button_expresion = ttk.Button(text="^", command=lambda: imprimir("^"))
button_expresion.place(x=310, y=400, width=65, height=40)
button_expresion = ttk.Button(text="sin", command=lambda: imprimir("sin"))
button_expresion.place(x=310, y=250, width=65, height=40)
button_expresion = ttk.Button(text="cos", command=lambda: imprimir("cos"))
button_expresion.place(x=240, y=250, width=65, height=40)
button_expresion = ttk.Button(text="tan", command=lambda: imprimir("tan"))
button_expresion.place(x=170, y=250, width=65, height=40)
button_expresion = ttk.Button(text="asin", command=lambda: imprimir("asin"))
button_expresion.place(x=100, y=250, width=65, height=40)
button_expresion = ttk.Button(text="acos", command=lambda: imprimir("acos"))
button_expresion.place(x=30, y=250, width=65, height=40)
button_expresion = ttk.Button(text="atan", command=lambda: imprimir("atan"))
button_expresion.place(x=310, y=200, width=65, height=40)
button_expresion = ttk.Button(text="log", command=lambda: imprimir("log"))
button_expresion.place(x=240, y=200, width=65, height=40)
button_expresion = ttk.Button(text="(", command=lambda: imprimir("("))
button_expresion.place(x=100, y=200, width=65, height=40)
button_expresion = ttk.Button(text=")", command=lambda: imprimir(")"))
button_expresion.place(x=170, y=200, width=65, height=40)
ventana.mainloop()
