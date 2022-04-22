num = int(input('Diga um numero inteiro: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
if cont == 2:
    verb = str('E POR ISSO ELE É PRIMO')
else:
    verb = str('E POR ISSO ELE NÂO É PRIMO')
print(f'\n\033[mO numero {num} foi dividido {cont} vezes')
