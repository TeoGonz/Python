def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input('Inserte la base: '))
exponente = int(input('Inserte el exponente: '))
pot = potencia(base, exponente)
print('La potencia de', base, 'elevado a', exponente, 'es', pot)