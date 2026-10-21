"""
Caso7
Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada

empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.
"""

cantidad_empleados = 2

id_empleado_1 = 8
edad_1 = 20
antiguedad_1 = 2

id_empleado_2 = 4
edad_2 = 30
antiguedad_2 = 3

suma_antiguedad_1 = 0
for k in range(1, antiguedad_1 + 1):
    suma_antiguedad_1 = suma_antiguedad_1 + k

sueldo_1 = (100 + edad_1 + suma_antiguedad_1) / antiguedad_1
print("Sueldo empleado", id_empleado_1, ":", sueldo_1)

suma_antiguedad_2 = 0
for k in range(1, antiguedad_2 + 1):
    suma_antiguedad_2 = suma_antiguedad_2 + k

sueldo_2 = (100 + edad_2 + suma_antiguedad_2) / antiguedad_2
print("Sueldo empleado", id_empleado_2, ":", sueldo_2)

total_nomina = sueldo_1 + sueldo_2
print("Nómina:", total_nomina)

if sueldo_1 > sueldo_2:
    mayor = id_empleado_1
    menor = id_empleado_2
elif sueldo_2 > sueldo_1:
    mayor = id_empleado_2
    menor = id_empleado_1
else:
    mayor = id_empleado_1
    menor = id_empleado_2

print("Mayor:", mayor)
print("Menor:", menor)