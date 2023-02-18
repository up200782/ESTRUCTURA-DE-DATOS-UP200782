import random
aleatorios = random.sample(range(100, 500), 100)
lista = aleatorios
valor = 404


def Bubblesort(lista):
    l = 0
    for i in range(0, len(lista)-1):
        for l in range(0, len(lista)-1-l):
            a = lista[l]
            b = lista[l+1]
            if (a > b):
                lista[l] = b
                lista[l + 1] = a
    return lista
def BinarySearch(lista, valor):
    inicio = 0
    final = 99
    mitad = inicio + final // 2
    i = 1
    while inicio <= final and lista[mitad] != valor:
        if (valor < lista[mitad]):
            final = mitad - 1
        else:
            inicio = mitad + 1
        i += 1
        mitad = (inicio+final)//2
    if (lista[mitad] == valor):
        lug = mitad
    else:
        lug = None
    return (lug, i)


lista = Bubblesort(lista)
p = BinarySearch(lista, valor)
print(p)
for i in range(0, (len(lista))):
    print(lista[i], end=" ")
    if ((i + 1) % 10 == 0):
        print("\n")
