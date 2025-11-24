nome = 'Gustavo Freitas'
idade = 22
altura = 1.82
peso = 77
imc = peso / altura ** 2

"f-strings, o F é de formatação da string"

linha_1 = f'meu nome é {nome}, tenho {idade} anos, tenho {altura} de altura e peso {peso}kg e meu imc é {imc:.2f}' 
#nessas parte de {imc:.5f} é para botar quantas casas decimais eu quero em um numero!

print(linha_1)