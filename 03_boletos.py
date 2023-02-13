n = 1000
x = 0
dinero = 0

boletos = []

while dinero <= n:
    x += 1
    dinero += x
    boletos.append(x)

dinero = n - (dinero - x)
x -= 1
boletos.pop()

print(len(boletos), "Boletos")
print("Te sobra", dinero)