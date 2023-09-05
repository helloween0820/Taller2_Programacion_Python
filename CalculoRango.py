# Solicitar al usuario la cantidad de valores a ingresar
n = int(input("¿Cuántos valores ingresará? "))

# Inicializar list para almacenar los datos
datos = []

# Solicitar al usuario que ingrese los datos uno por uno
for i in range(1, n + 1):
    valor = float(input(f"Valor {i}: "))
    datos.append(valor)

# Calcular el rango de los datos
rango = max(datos) - min(datos)

# Mostrar el resultado
print(f"El rango es {rango:.2f}")
