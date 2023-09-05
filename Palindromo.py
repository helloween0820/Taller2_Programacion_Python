def es_palindromo(numero):
    # Convertir el número a una cadena para facilitar la comparación de caracteres
    numero_str = str(numero)

    # Comparar la cadena original con su versión invertida
    if numero_str == numero_str[::-1]:
        return True
    else:
        return False


# Solicitar al usuario que ingrese un número
numero = input("Ingrese un numero: ")

# Verificar si el número ingresado es un palíndromo
if es_palindromo(numero):
    print(numero, "es palindromo")
else:
    print(numero, "no es palindromo")
