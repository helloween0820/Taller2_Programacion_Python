positivos = 0
negativos = 0

print("Ingrese varios valores, termine con cero:")

while True:
    valor = int(input())

    if valor == 0:
        break

    if valor > 0:
        positivos += 1
    else:
        negativos += 1

print("Positivos:", "*" * positivos)
print("Negativos:", "*" * negativos)
