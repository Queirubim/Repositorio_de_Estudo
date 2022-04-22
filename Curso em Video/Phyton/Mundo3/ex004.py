tup1 = (int(input('Digite um número: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
print(f'Voçê digitou os numeros {tup1}')
print(f'O valor 9 apareceu {tup1.count(9)} vezes.')
if 3 in tup1:
    print(f'O valor 3 apareceu na {tup1.index(3)} posição.')
else:
    print('O numero 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for g in tup1:
    if g % 2 == 0:
        print(g, end=' ')
