def multiplication(a, b):
    if b == 0:
        return 0
    return a + multiplication(a, b - 1)

a = int(input('Inserte el primer numero: '))
b = int(input('Inserte el segundo numero: '))
result = multiplication(a, b)
print('El resultado de la multiplicacion es', result)