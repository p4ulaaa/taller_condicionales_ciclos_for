"""
Caso1:
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.
"""

limite_a = int(input("Ingrese el limite a: "))
limite_b = int(input("Ingrese el limite b: "))

if -100 <= limite_a <= 100 and -100 <= limite_b <= 100:
    if limite_a < limite_b :
        for num in range(limite_a, limite_b + 1):
            print(num)

    elif limite_a == limite_b :
        print(limite_a)

    else:
        for num in range(limite_a, limite_b - 1, -1):
            print(num)
else:
    print("Error: limites invalidos")