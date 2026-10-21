"""
Ejemplo:
Mostrar en pantalla si un numero entero ingresado por el usuario es positivo o no lo es.

ENTRADA
- num: numero entero ingresado por el usuario

PROCESO
- si num > 0 entonces
    mostrar: el numero ingresado es positivo.

    si no
    mostrar: el numero ingresado no es positivo.

SALIDA
- Mostrar en pantall si el numero entero ingresado es positivo o no es positivo.
"""

num = int(input("Ingrese un numero entero: "))

if num > 0:
    print("El número es positivo")

else:
    print("El numero es negativo")