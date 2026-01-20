'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''

condicao = True

'''while condicao:
    nome = input("Qual seu nome? ")
    print(f"Seu nome é {nome}")

    if nome == "sair":
        break
'''

contador = 0

'''while contador < 10:
    contador = contador + 1
    print(f"Seu número agora é {contador}")
'''

numerador = 0

'''while numerador <= 100:
    numerador += 1

    if numerador == 10:
        print('Cade o 10????')
        continue

    if numerador >= 15 and numerador <= 20:
        print(f'Não vou mostrar o {numerador}')
        continue

    print(numerador)

    if numerador == 40:
        print("Parou no 40 nenem")
        break

print("Acabou")
'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1

'''while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha = }, {coluna = }')
        coluna += 1

    linha += 1

print("Acabou")'''

frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum"

i = 0

while i < len(frase):
    letra_atual = frase[i]
    qtd_letras_aparece = frase.count(letra_atual)

    print(letra_atual, qtd_letras_aparece)
    i += 1