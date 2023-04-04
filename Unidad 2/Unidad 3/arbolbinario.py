class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def agregar_a_arbol(raiz, valor):
    if raiz is None:
        raiz = Nodo(valor)
    elif valor < raiz.valor:
        raiz.izquierda = agregar_a_arbol(raiz.izquierda, valor)
    else:
        raiz.derecha = agregar_a_arbol(raiz.derecha, valor)
    return raiz

def imprimir_arbol(raiz, nivel=0):
    if raiz is None:
        return
    imprimir_arbol(raiz.derecha, nivel+1)
    print(' '*4*nivel + '->', raiz.valor)
    imprimir_arbol(raiz.izquierda, nivel+1)

def recorrido_infix(raiz):
    if raiz:
        recorrido_infix(raiz.izquierda)
        print(raiz.valor, end=" ")
        recorrido_infix(raiz.derecha)

def recorrido_postfix(raiz):
    if raiz:
        recorrido_postfix(raiz.izquierda)
        recorrido_postfix(raiz.derecha)
        print(raiz.valor, end=" ")

def recorrido_prefix(raiz):
    if raiz:
        print(raiz.valor, end=" ")
        recorrido_prefix(raiz.izquierda)
        recorrido_prefix(raiz.derecha)

def recorrido_nivel(raiz):
    if raiz is None:
        return
    queue = []
    queue.append(raiz)
    while(len(queue) > 0):
        print(queue[0].valor, end=" ")
        node = queue.pop(0)
        if node.izquierda is not None:
            queue.append(node.izquierda)
        if node.derecha is not None:
            queue.append(node.derecha)

# Creamos un árbol binario con la palabra "hola"
palabra = "hola"
raiz = None
for letra in palabra:
    raiz = agregar_a_arbol(raiz, letra)

# Imprimimos el árbol
imprimir_arbol(raiz)

# Imprimimos los recorridos del árbol
print("Recorrido infix: ", end="")
recorrido_infix(raiz)
print()

print("Recorrido postfix: ", end="")
recorrido_postfix(raiz)
print()

print("Recorrido prefix: ", end="")
recorrido_prefix(raiz)
print()

print("Recorrido a nivel: ", end="")
recorrido_nivel(raiz)
print()
