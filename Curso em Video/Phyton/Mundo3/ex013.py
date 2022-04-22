pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados. append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    stop = str(input('Continuar ? [S/N]: '))
    if stop in 'nN':
        break
    dados.clear()

print(f'O numero de pessoas cadastradas foram {len(pessoas)}.')
print(f'O maior peso foi de {maior}kg. ', end='')
for p in pessoas:
    if maior == p[1]:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor}kg. ', end='')
for p in pessoas:
    if menor == p[1]:
        print(f'[{p[0]}]', end=' ')
