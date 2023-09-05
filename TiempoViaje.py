total_minutes = 0

while True:
    duracion_tramo = int(input("Duracion tramo: "))

    if duracion_tramo == 0:
        break

    total_minutes += duracion_tramo

horas = total_minutes // 60
minutos = total_minutes % 60

print(f"Tiempo total de viaje: {horas}:{minutos:02} horas")
