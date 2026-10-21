"""
Caso6
Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
"""

cantidad_ciclistas = 2

identificador_1 = 10
minutos_1 = 0
segundos_1 = 25
centesimas_1 = 0

identificador_2 = 20
minutos_2 = 0
segundos_2 = 20
centesimas_2 = 0

tiempo_total_1 = (60 * minutos_1) + segundos_1 + (centesimas_1 / 100)
velocidad_1 = 900 / tiempo_total_1
print("Ciclista", identificador_1, "Velocidad:", velocidad_1, "km/h")

tiempo_total_2 = (60 * minutos_2) + segundos_2 + (centesimas_2 / 100)
velocidad_2 = 900 / tiempo_total_2
print("Ciclista", identificador_2, "Velocidad:", velocidad_2, "km/h")

if tiempo_total_1 < tiempo_total_2:
    ganador = identificador_1
else:
    ganador = identificador_2

print("Ganador:", ganador)