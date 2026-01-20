dias_atraso = int(input("Quantos dias após a data de vencimento voce devolveu o livro? "))
multa = 0

if dias_atraso <= 3:
    multa = dias_atraso * 0,50
elif dias_atraso >= 4 and dias_atraso <= 7:
    multa = dias_atraso * 1
elif dias_atraso >= 8:
    multa = dias_atraso * 2

print(f"O valor da sua multa é de {multa:.2f}")