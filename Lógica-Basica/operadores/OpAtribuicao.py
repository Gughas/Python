"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 0

###

while contador <= 100:
    contador += 1

    if contador == 10:
        print('Cade o 10????')
        continue

    if contador >= 15 and contador <= 20:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        print("Parou no 40 nenem")
        break

print("Acabou")