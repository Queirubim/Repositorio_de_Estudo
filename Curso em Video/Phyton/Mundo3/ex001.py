num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', ' quinze', 'deseseis', 'desesete', 'desoito',
       'desenove', 'vinte')
operador = int(input('Diga um numero de 0 a 20: '))
while operador not in range(0, 20):
    print('Tente novamente.', end=' ')
    operador = int(input('Diga um numero de 0 a 20: '))
print(f'Voce digitou o numero {num[operador]}')
