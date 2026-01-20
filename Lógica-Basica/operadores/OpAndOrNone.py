# Operadores lógicos
# and(e) or(ou) not(não)
# and - Todas as condições precisam ser consideradas verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy 0, 0.0, '', false
#também existe o tipo none que é usada para representar um não valor

entrada = input('entrar ou sair: ')
senha_digitada = input('Senha: ') 
senha_permitida = '12345'

if (entrada == "Entrar" or entrada == "entrar") and senha_digitada == senha_permitida:
    print("Você entrou")
else: 
    print("some daqui seu newba do krl") 

# Avaliação de curto circuito
senha = input("senha: ") or "sem senha"
print(senha)



# Operador lógico "not"
# Usado para inverter expressões
# not true = false
# not false = true

minha_senha = input("Senha: ")

if not senha:
    print("você nao digitou nada")
    # quando não digita nada a expressão vira false, mas nesse caso o not ta invertendo, assim executando o código