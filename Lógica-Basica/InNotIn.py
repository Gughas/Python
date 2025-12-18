# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# G u s t a v o
#-7-6-5-4-3-2-1

nome = 'gustavo'


print("t" in nome)
print("gus" in nome)
print("avo" in nome)

print("t" not in nome)
print("zero" not in nome)
print("avo" not in nome)
 
name = input('Digite seu nome seu animal de teta: ')

if "Gustavo" in name:
    print('BEM VINDUUU :3')
else:
    print('VOCE É FALSO, NAO É O VERDADEIRO GUGU')


objeto = input('digite algo: ')
encontrar = input('Digite o que vc quer achar: ')

if encontrar in objeto: 
    print(f'{encontrar} está em {objeto}, ACHPOOOOOOOO')
else:
    print(f'{encontrar} nao esta em {objeto}, CARALHO MANE BURRAO PQP')