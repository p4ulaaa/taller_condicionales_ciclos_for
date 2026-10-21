"""
Caso5
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.

"""


n = 5
v1 = 0
v2 = 200
v3 = 201
v4 = 399
v5 = 400


grupo1 = 0
grupo2 = 0
grupo3 = 0

for i in range(n):
    if i == 0:
        v = v1
    elif i == 1:
        v = v2
    elif i == 2:
        v = v3
    elif i == 3:
        v = v4
    else:
        v = v5
        
    if v <= 200:
        grupo1 = grupo1 + 1
    elif v < 400:
        grupo2 = grupo2 + 1
    else:
        grupo3 = grupo3 + 1

# SALIDA
print("Grupos 1, 2 y 3:", grupo1, ";", grupo2, ";", grupo3)
