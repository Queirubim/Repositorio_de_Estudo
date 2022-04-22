print('===========Financeamento===========')
salario = float(input('Diga o Valor do seu salario : '))
casa = float(input('\033[32mDiga o valor da casa que deseja :\033[m '))
prestacao = int(input('Em quantos anos deseja pagar : '))
mensal = casa / (prestacao * 12)
if mensal < salario*30/100:
    print('\033[32mSeu Empretimo Foi Aprovado !!!\033[m')
    print(f'Voce pagara R$:{mensal:.2f} por {prestacao*12} meses.')
else:
    print('\033[31mEmprestimo Reprovado !!!\033[m')
    print(f'A prestação R$:{mensal:.2f} foi maior a 33% do seu salario que é R$:{(salario*30)/100}.')
