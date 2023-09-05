# Inicializamos una lista para almacenar los números ingresados
numeros = []

# Solicitamos al usuario ingresar números hasta que ingrese "."
while True:
    entrada = input("Ingrese un número o '.' para terminar: ")

    if entrada == ".":
        break

    numero = float(entrada)
    numeros.append(numero)

# Ordenamos la lista de números
numeros.sort()

# Calculamos la mediana
n = len(numeros)
if n % 2 == 1:  # Cantidad de números impar
    mediana = numeros[n // 2]
else:  # Cantidad de números par
    indice1 = n // 2 - 1
    indice2 = n // 2
    mediana = (numeros[indice1] + numeros[indice2]) / 2

# Mostramos la mediana
print(f"La mediana es {mediana}.")
