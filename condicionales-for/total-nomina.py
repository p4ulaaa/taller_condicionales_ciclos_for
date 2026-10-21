"""
Caso3:
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
"""
numero_empleados = int(input("Ingrese el numero de empleados: "))

suma = 0.0

if 0 <= numero_empleados <= 1000:
    for veces in range(1, numero_empleados + 1):
        print("Empleado #", veces)
        sueldo = input("sueldo? ")
        suma = suma + sueldo #<= acumuladores

else:
    print("no valido")
print("La nomina es:", suma)

    


