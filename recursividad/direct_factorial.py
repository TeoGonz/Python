def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input('Inserte un numero entero para calcular su factorial: '))
fact = factorial(num)
print('El factorial de', num, 'es', fact)