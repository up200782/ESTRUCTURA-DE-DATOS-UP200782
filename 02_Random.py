from random import randrange

print("Numero Secreto")
print("Selecione una dificultad , 1 = FACIL(1 al 100) 2 = INTERMEDIO(1 al 500) 3 = DIFICIL(1 al 1000)")

dificultad = int(input())
num_secreto = randrange(1, 100 if dificultad == 1 else 500 if dificultad == 2 else 1000)

d = 0
while True: 
    c = int(input("Dime el numero secreto: "))
    d += 1
    if c == num_secreto:
        print(f"Felicidades... Lo hiciste en {d} intentos")
        break
    elif c > num_secreto:
        print("Abajo")
    elif c < num_secreto:
        print("Arriba")