v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
print('''[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos Numeros
[5] Sair''')
c = 0
while c != 5:
    c = int(input('Sua escolha: '))
    if c == 4:
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))
    if c == 1:
        print(f'{v1} + {v2} = {v1+v2}')
    if c == 2:
        print(f'{v1} X {v2} = {v1*v2}')
    if c == 3:
        if v1 > v2:
            print(f'O {v1} é o maior.')
        elif v1 == v2:
            print(f'O {v1} e o {v2} são iguais')
        else:
            print(f'O {v2} é o maior.')
print('FIM DO PROGRAMA !')
