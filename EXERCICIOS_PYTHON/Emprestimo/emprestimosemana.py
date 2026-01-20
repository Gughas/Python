total_emprestimos = 0
maior_emprestimo = 0
dia_maior_emprestimo = 0

for dia in range(1, 8):
    emprestimo = int(input(f'Qual foi a quantidade de empréstimo no dia {dia}:'))
    total_emprestimos += emprestimo

    media = total_emprestimos / 7

    if emprestimo > maior_emprestimo:
        maior_emprestimo = emprestimo
        dia_maior_emprestimo = dia
    
print(f"A média de livros emprestados na semana é de {media:.0f}")
print(f"Dia com maior número de empréstimos: {dia_maior_emprestimo}")





