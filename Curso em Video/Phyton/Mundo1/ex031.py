sa = float(input('Qual é o seu salario : '))
if sa <= 1250:
    aum = 15
else:
    aum = 10
print(f'Voçê teve um aumento de \033[4;32m{aum}\033[m% seu novo salario é R$:\033[7;30m{sa*aum/100+sa:.2f}\033[m')
