''' CALCULADORA COM WHILE '''

while True:

    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    opr = input("Digite o operador: (+, -, /, *): ")

    num1_float = 0
    num2_float = 0


    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um dos números são inválidos")
        continue


    operador_permitido = "+-/*"

    if opr not in operador_permitido:
        print("Digite um operador permitido!")
        continue

    if len(opr) > 1:
        print('Digite apenas um operador')
        continue

    if opr == "+":
        print(f"{num1_float} + {num2_float} = ", num1_float + num2_float)
    elif opr == "-":
        print(f"{num1_float} - {num2_float} = ", num1_float - num2_float)
    elif opr == "/":
        print(f"{num1_float} / {num2_float} = ", num1_float / num2_float)
    elif opr == "*":
        print(f"{num1_float} * {num2_float} = ", num1_float * num2_float)

    ############
    
    sair = input("Deseja Sair? [s]: ").lower().startswith("s")

    if sair is True:
        break