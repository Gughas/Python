nome = "Gustavo"
sobrenome = 'Freitas'
idade = 22
altura = 1.80
peso = 82
imc = peso / altura ** 2

# tambem invés de chamar os parâmetros em ordem, podemos chamar pelos indices, assim podendo repetir o parâmetro
"""string = 'meu nome é {0} {1}, atualmente tenho {2} anos de idade, tenho {3} de altura e peso {4}kg e meu imc é {5:.3f} e lembrando meu nome é {0} {1}'
formato = string.format(nome, sobrenome, idade, altura, peso, imc)"""

#tambem podemos nomear os parâmetros, assim ficando mais facil de entender o código
string = 'meu nome é {nome} {sobrenome}, atualmente tenho {idade} anos de idade, tenho {altura} de altura e peso {peso}kg e meu imc é {imc:.3f} e lembrando meu nome é {nome} {sobrenome}'
formato = string.format(
    nome = nome, 
    sobrenome = sobrenome, 
    idade = idade, 
    altura = altura, 
    peso = peso, 
    imc = imc)

print(formato)