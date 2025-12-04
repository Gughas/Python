primeiro_valor = int(input("Digite um numero:"))
segundo_valor = int(input("Digite um outro numero:"))

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior que o {segundo_valor}")
elif primeiro_valor < segundo_valor:
    print(f"{segundo_valor} é maior que o {primeiro_valor}")
else:
    print("Mas tu é burro em cara, os dois são iguais")