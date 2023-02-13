def ecuacion(y):     # x'2-8x+15
    resultado = float
    resultado = (y**2) - (8*y) + 15
    return resultado

limite_inferior = 4
limite_superior = 7
punto_medio = float

precision_esperada = 0.0001
error = abs(limite_superior - limite_inferior)
contador = 0

while error > precision_esperada:
    punto_medio = (limite_inferior + limite_superior) / 2
    y1 = ecuacion(limite_inferior)
    y2 = ecuacion(punto_medio)
    if y1 * y2 < 0:
        limite_superior = punto_medio
    else:
        limite_inferior = punto_medio
    error = abs(limite_superior - limite_inferior)
    contador += 1

print(f"Iteraciones: {contador}, Raíz: {punto_medio}")
