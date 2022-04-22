lis = []
lis_par = []
lis_impar = []
while True:
    lis.append(int(input('Digite um numero: ')))
    stop = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if stop == 'N':
        break
for numero in lis:
    if numero % 2 == 0:
        lis_par.append(numero)
    else:
        lis_impar.append(numero)
print('-'*40)
print(f'A lista completa é {lis}')
print(f'A lista com numeros par é {lis_par}')
print(f'A lista com numeres impares é {lis_impar}')
