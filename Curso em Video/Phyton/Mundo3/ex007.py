valores = list()
for v in range(1, 6):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print('-'*40)
print(f'Voçê digitou os valores {valores}')
print(f'o maior valor digitado foi {max(valores)} nas posiçãoes ', end='')
for ma, v1 in enumerate(valores):
    if v1 == max(valores):
        print(f'{ma+1}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posiçãoes ', end='')
for mi, v2 in enumerate(valores):
    if v2 == min(valores):
        print(f'{mi+1}... ', end='')
