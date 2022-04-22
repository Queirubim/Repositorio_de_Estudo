valores = list()
p = ' '
c = 0
while p not in 'N':
    valores.append(int(input('Digite um valor: ')))
    if c > 0 and valores[-1] in valores[0:-1]:
        valores.pop()
        print('Valor duplicado! Não vou adicionar... ')
    else:
        print('Valor adicionado com secesso...')
    c += 1
    p = str(input('Valor adicionado quer continuar? [S/N]:')).strip().upper()[0]
    valores.sort()
print('-'*40)
print(f'Vice digitou os valores {valores}')
