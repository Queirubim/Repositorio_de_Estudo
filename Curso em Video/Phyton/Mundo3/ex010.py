lis = []
while True:
    lis.append(int(input('Digite um numero inteiro: ')))
    res = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('-'*40)
print(f'Foram digitados {len(lis)} numeros. ')
lis.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lis}')
if 5 in lis:
    print(f'O valor 5 foi digitado na posição {lis.index(5)} da lista.')
else:
    print('O valor 5 não foi digitado na lista.')
